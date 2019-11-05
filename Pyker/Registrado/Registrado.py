import pyautogui
from datetime import datetime

class Registrado:

    def __init__(self,lista_de_cartas=[],telas_por_colunas=2):
        self.lista_de_cartas = lista_de_cartas
        self.telas_por_colunas = telas_por_colunas
        self.lista_de_telas = []
        self.listar_telas()

    def listar_telas(self):
        dicionario_de_telas = pyautogui.getWindows()
        for tela in self.lista_de_telas: tela['ativo'] = False
        for titulo in dicionario_de_telas:
            if titulo.find("No Limit Hold'em") != -1:
                nova_tela = {'titulo':titulo,'ativo':False,'recorte':()}
                if nova_tela not in self.lista_de_telas:
                    nova_tela['ativo'] = True
                    self.lista_de_telas.append(nova_tela)
                else:
                    index = self.lista_de_telas.index(nova_tela)
                    self.lista_de_telas[index]['ativo'] = True


    def organizar_telas(self,divisoes=2,proporcao=1.35,deslocamento=(- 10,- 20,0,- 10),rodape= - 20):
        tamanho_da_tela = pyautogui.size()
        altura = int((tamanho_da_tela[1] + rodape)/divisoes)
        largura = int(altura * proporcao)
        for idx,tela in enumerate(self.lista_de_telas):
            janela = pyautogui.getWindow(tela['titulo'])
            posicao_x = (largura + deslocamento[1])* int( idx / divisoes) + deslocamento[0]
            posicao_y = (altura + deslocamento[3])* int( idx % divisoes) + deslocamento[2]
            dupla = (posicao_x,posicao_y,largura,altura)
            tela['recorte'] = dupla
            janela.resize( largura, altura)
            janela.move(posicao_x,posicao_y)

    def registrar(self,tela,data=None):
        data = datetime.now() if data == None else data
        chave = self.gerar_chave(tela,data)
        carta = {'titulo':self.lista_de_telas[tela]['titulo'],
                 'tela':tela,
                 'data':data.strftime("%Y-%m-%d %H:%M:%S.%f"),
                 #'data_dia':data.strftime("%Y-%m-%d"),
                 #'data_hora':data.strftime("%H-%M-%S-%f"),
                 'chave':chave,
                 'recorte':self.lista_de_telas[tela]['recorte'],

                 'foto':None,
                 'fotografo_processado': False,
                 'endereco_imegem': '',
                 #'foto_registrada': False,
                 'foto_salvo': False,

                 'cena': None,
                 'cenografo_processado': True,
                 'cena_salvo': False,

                 'cientista_processado': False,
                 'cientista_salvo': False,

                 'mesa':0,
                 'nova_carta':True,
                 }

        self.lista_de_cartas.append(carta)
        index = len(self.lista_de_cartas) - 1
        return index

    def gerar_chave(self,ordem_da_tela,data=datetime.now()):
        return "".join([data.strftime('%Y%m%d%H%M%S'),'-',str(ordem_da_tela),'-','00'])

    def quantidade_de_cartas_registradas(self,tela,categoria):
        quantidade_itens_registrados = 0
        for carta in self.lista_de_cartas:
            if carta['tela'] == tela and carta[categoria] != None:
                quantidade_itens_registrados += 1
        return quantidade_itens_registrados





