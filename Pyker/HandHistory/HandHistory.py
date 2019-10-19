import re
from copy import copy, deepcopy
from pprint import pprint

class HandHistory:

    def __init__(self):
        self.mao = {}
        self.maos = []
        self.ficheiro_base = {}
        self.lista_de_ficherios = []
        self.nova_mao = True
        self.numero_da_mao = 0
        self.etapa_atual = 'null'
        self.arquivo = ''

    def gerar_lista_de_ficheiros(self):
        self.percorrer_historico_de_mao()
        return self.maos

    def percorrer_historico_de_mao(self):
        caminho = self.arquivo
        f = open(caminho, 'r')
        for linha in f:
            if self.e_nova_mao(linha) == True:
                self.mao = self.limpar_mao()
            elif self.e_fim_da_mao(linha) == True:
                self.gerar_ficheiro_inicial()
                self.percorrer_jogadas_e_gerar_ficheiro()
            self.estrair_dados(linha)
        f.close()

    def e_nova_mao(self,linha):
        mao_nova = False
        if self.nova_mao == True and linha != '\n':
            mao_nova = True
            self.numero_da_mao += 1
            self.nova_mao = False
        return mao_nova

    def e_fim_da_mao(self,linha):
        fim_da_mao = False
        if self.nova_mao == False and linha == '\n':
            fim_da_mao = True
            self.nova_mao = True
        return fim_da_mao

    def limpar_mao(self):
        self.etapa_atual = 'null'
        mao = {'cabecalho': {'site': 'null', 'estilo': 'null', 'id_hand': 0, 'modalidade': 'null', 'blind': 'null',
                             'data': 'null', 'lugares':'null', 'botao':'null'},
               'jogadores': {}, 'etapas':{'HOLE CARDS':[],'FLOP':[],'TURN':[],'RIVER':[],'SHOW DOWN':[],'SUMMARY':[]}}
        return mao

    def estrair_dados(self,linha):
        self.cabelcalho_1(linha)
        self.cabelcalho_2(linha)
        self.jogadores(linha)
        self.small_blind(linha)
        self.big_blind(linha)
        self.hole_cards_do_hero(linha)
        self.etapas(linha)
        self.jogadas(linha)
        self.cartas_amostra(linha)

    def cabelcalho_1(self,linha):
        exprecao = r"(^\w+)\s(.+)\s#(\d+):\s+(.*)(\(\$(\d+.\d+?)/\$(\d+.\d+?)\))\s+-\s+((\d+/\d+/\d+)\s+(\d+:\d+:\d+))"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            self.mao['cabecalho']['site'] = palavras[0][0]
            self.mao['cabecalho']['estilo'] = palavras[0][1]
            self.mao['cabecalho']['id_hand'] = palavras[0][2]
            self.mao['cabecalho']['modalidade'] = palavras[0][3]
            self.mao['cabecalho']['blind'] = palavras[0][4]
            self.mao['cabecalho']['data'] = palavras[0][7]

    def cabelcalho_2(self,linha):
        exprecao = r"^\w+\s+'\w+'\s+(\d-\w+)\s\w+\s#(\d)\s\w+\s\w+\s\w+"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            self.mao['cabecalho']['lugares'] = palavras[0][0]
            self.mao['cabecalho']['botao'] = int(palavras[0][1])

    def jogadores(self,linha):
        exprecao = r"^\w+\s+(\d):\s+(.*)\s+\(\$(\d*.?\d+)\sin\schips"
        palavras = re.findall(exprecao, linha)
        letras = ['A','B','C','D','E','F']
        numero_de_jogadores = len(self.mao['jogadores'])
        botao = self.mao['cabecalho']['botao']
        if len(palavras) > 0:
            posicao_rel = self.posicao_relativa(botao , int(palavras[0][0]))
            self.mao['jogadores'][palavras[0][1]] = {'letra':letras[numero_de_jogadores],
                                                     'posicao':int(palavras[0][0]),
                                                     'posicao_relativa':posicao_rel,
                                                     'fichas':palavras[0][2],
                                                     'aposta':0.00,
                                                     'cartas':[],
                                                     'heroi':False}

    def posicao_relativa(self,botao,posicao):
        posicoes = ['SB','BB','UTG','MP','CO','BTN']
        posicao_relativa_index = posicao - botao - 1
        if posicao_relativa_index > 0:
            return posicoes[posicao_relativa_index]
        else:
            return posicoes[(posicao_relativa_index + 5)]


    def small_blind(self,linha):
        exprecao = r"(^.*):\s+\w+\s+small\s+blind\s+\$(\d*.?\d+)"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            self.mao['jogadores'][palavras[0][0]]['posicao_relativa'] = 'SB'
            self.mao['jogadores'][palavras[0][0]]['aposta'] = palavras[0][1]

    def big_blind(self,linha):
        exprecao = r"(^.*):\s+\w+\s+big\s+blind\s+\$(\d*.?\d+)"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            self.mao['jogadores'][palavras[0][0]]['posicao_relativa'] = 'BB'
            self.mao['jogadores'][palavras[0][0]]['aposta'] = palavras[0][1]

    def hole_cards_do_hero(self,linha):
        exprecao = r"^Dealt\s+to\s+(.*)\s+\[(\w+)\s+(\w+)]"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            self.mao['jogadores'][palavras[0][0]]['cartas'] = [palavras[0][1],palavras[0][2]]
            self.mao['jogadores'][palavras[0][0]]['heroi'] = True

    def etapas(self,linha):
        exprecao = r"^\*{3}\s+(.*)\s+\*{3}\s+(\[((\w+\s*){3,5})\]\s+(\[(\w+)\])?)?"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            self.etapa_atual = palavras[0][0]
            if palavras[0][0] == 'HOLE CARDS':
                self.mao['etapas'][self.etapa_atual] = {'jogadas': []}
            elif palavras[0][0] == 'FLOP' or palavras[0][0] == 'TURN' or palavras[0][0] == 'RIVER':
                cartas = palavras[0][2]
                cartas = cartas.split(" ")
                cartas.append(palavras[0][5])
                cartas.append('')
                self.mao['etapas'][self.etapa_atual] = {'bord':cartas,'jogadas':[]}
            else:
                self.mao['etapas'][self.etapa_atual] = {}

    def jogadas(self,linha):
        exprecao = r"(^.*):\s+(folds|calls|bets|raises|checks)(\s+\$(\d*.?\d+)(\s+\w+\s+\$(\d*.?\d+))?)?"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            valor = float(palavras[0][3]) if len(palavras[0][3]) >= 1 else 0.00
            valor_r = float(palavras[0][5]) if len(palavras[0][5]) >= 1 else 0.00
            self.mao['etapas'][self.etapa_atual]['jogadas'].append({'jogador': palavras[0][0],
                                                                    'movimento': palavras[0][1],
                                                                    'valor': valor,
                                                                    'valor_r': valor_r})

    def cartas_amostra(self,linha):
        exprecao = r"^(.*):\s+shows\s+\[(\w+)\s(\w+)]"
        palavras = re.findall(exprecao, linha)
        if len(palavras) > 0:
            self.mao['jogadores'][palavras[0][0]]['cartas'] = [palavras[0][1],palavras[0][2]]

    def gerar_ficheiro_inicial(self):
        ficheiro = {'fichas':{},'aposta':{},'hole_cards':{},'diler':{},'vez':{},'pote':{},'combo':{},
                    'pote_rodada':{},'bord':{},'tela':{'A':0}}
        ficheiro['pote']['A'] = 0
        ficheiro['pote_rodada']['A'] = 0.00
        ficheiro['bord'] = {'FLOP_1':'','FLOP_2':'','FLOP_3':'','TURN':'','RIVER':''}
        for jogadores in self.mao['jogadores']:
            letra = self.mao['jogadores'][jogadores]['letra']
            ficheiro['fichas'][letra] = float(self.mao['jogadores'][jogadores]['fichas'])
            ficheiro['aposta'][letra] = float(self.mao['jogadores'][jogadores]['aposta'])
            ficheiro['combo'][''.join([letra,'_1'])] = ''
            ficheiro['combo'][''.join([letra,'_2'])] = ''
            ficheiro['pote']['A'] += ficheiro['aposta'][letra]
            ficheiro['vez'][letra] = False
            ficheiro['diler'][letra] = False
            ficheiro['hole_cards'][letra] = False
            if self.mao['cabecalho']['botao'] == self.mao['jogadores'][jogadores]['posicao']:
                ficheiro['diler'][letra] = True
            if self.mao['jogadores'][jogadores]['posicao_relativa'] == 'UTG':
                ficheiro['vez'][letra] = True
        self.ficheiro_base = ficheiro
        self.maos.append(deepcopy(ficheiro))

    def percorrer_jogadas_e_gerar_ficheiro(self):
        etapas = ['HOLE CARDS','FLOP','TURN','RIVER','SHOW DOWN','SUMMARY']
        for etapa in etapas:
            if len(self.mao['etapas'][etapa]) > 0:
                self.alteracoes_da_mudanca_de_etapa(etapa)
                for jogada in self.mao['etapas'][etapa]['jogadas']:
                    self.converter_jogada_em_ficheiro(jogada)

    def converter_jogada_em_ficheiro(self,jogada):
        jogador = jogada['jogador']
        letra = self.mao['jogadores'][jogador]['letra']
        valor = jogada['valor'] if jogada['valor_r'] == 0.00 else jogada['valor_r']
        for letra_vez in ['A', 'B', 'C', 'D', 'E', 'F']:
            self.ficheiro_base['vez'][letra_vez] = False
        self.ficheiro_base['vez'][self.letra_a_direita(letra)] = True
        if jogada['movimento'] in ['bets','raises','calls']:
            valor_anterior = self.ficheiro_base['aposta'][letra]
            diferenca = valor - valor_anterior
            self.ficheiro_base['aposta'][letra] = valor
            self.ficheiro_base['fichas'][letra] -= diferenca
            self.ficheiro_base['pote']['A'] += diferenca
            self.ficheiro_base['pote']['A'] = round(self.ficheiro_base['pote']['A'], 2)
            fichas = self.ficheiro_base['fichas'][letra]
            self.ficheiro_base['fichas'][letra] = round(fichas, 2)
        elif jogada['movimento'] == 'folds':
            self.ficheiro_base['hole_cards'][letra] = True
        self.lista_de_ficherios.append(deepcopy(self.ficheiro_base))

        self.maos.append(deepcopy(self.ficheiro_base))


    def alteracoes_da_mudanca_de_etapa(self,etapa):
        if etapa in ['FLOP','TURN','RIVER']:
            for letra in ['A','B','C','D','E','F']:
                self.ficheiro_base['aposta'][letra] = 0
            self.ficheiro_base['bord']['FLOP_1'] = self.mao['etapas'][etapa]['bord'][0]
            self.ficheiro_base['bord']['FLOP_2'] = self.mao['etapas'][etapa]['bord'][1]
            self.ficheiro_base['bord']['FLOP_3'] = self.mao['etapas'][etapa]['bord'][2]
            self.ficheiro_base['bord']['TURN'] = self.mao['etapas'][etapa]['bord'][3]
            self.ficheiro_base['bord']['RIVER'] = self.mao['etapas'][etapa]['bord'][4]
            self.ficheiro_base['pote_rodada']['A'] = self.ficheiro_base['pote']['A']
            self.limpar_apostas_no_comeco_do_pos_flop()

    def limpar_apostas_no_comeco_do_pos_flop(self):
        for letra in ['A', 'B', 'C', 'D', 'E', 'F']:
            self.ficheiro_base['aposta'][letra] = 0.00
        self.maos.append(deepcopy(self.ficheiro_base))

    def letra_a_direita(self,letra):
        letras = ['A','B','C','D','E','F']
        index = letras.index(letra)
        for x in range(6):
            index = (index + 1) if index < 5 else 0
            if self.ficheiro_base['hole_cards'][letras[index]] == False:
                break
        return letras[index]
