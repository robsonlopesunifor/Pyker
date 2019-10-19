import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Analizar.Analizar_nome as Analizar

class Analizar_nome_test(unittest.TestCase):

    def test_analizar(self):
        analizar_nome = Analizar.Analizar_nome()
        dataframe = pd.DataFrame()
        analizar_nome.iniciar(dataframe)

        self.incrementar_dataframe(dataframe ,0)
        analizar_nome.analizar(0)
        assert analizar_nome.dataframe.loc[0 ,('nome_acao')] == 'FOLD'
        assert analizar_nome.dataframe.loc[0 ,('nome_bet')] == 'null'
        assert analizar_nome.dataframe.loc[0 ,('nome_jogada')] == 'null'
        assert analizar_nome.dataframe.loc[0 ,('nome_utima_bet')] == 'BB'
        assert analizar_nome.dataframe.loc[0 ,('nome_vilao')] == 'BB'


        self.incrementar_dataframe(dataframe ,1)
        analizar_nome.analizar(1)
        assert analizar_nome.dataframe.loc[1 ,('nome_acao')] == 'CALL'
        assert analizar_nome.dataframe.loc[1 ,('nome_bet')] == 'null'
        assert analizar_nome.dataframe.loc[1 ,('nome_jogada')] == 'null'
        assert analizar_nome.dataframe.loc[1 ,('nome_utima_bet')] == 'BB'
        assert analizar_nome.dataframe.loc[1 ,('nome_vilao')] == 'BB'

        self.incrementar_dataframe(dataframe ,2)
        analizar_nome.analizar(2)
        assert analizar_nome.dataframe.loc[2 ,('nome_acao')] == 'RAISE'
        assert analizar_nome.dataframe.loc[2 ,('nome_bet')] == 'OR'
        assert analizar_nome.dataframe.loc[2 ,('nome_jogada')] == 'null'
        assert analizar_nome.dataframe.loc[2 ,('nome_utima_bet')] == 'OR'
        assert analizar_nome.dataframe.loc[2 ,('nome_vilao')] == 'UTG'

        self.incrementar_dataframe(dataframe ,3)
        analizar_nome.analizar(3)
        assert analizar_nome.dataframe.loc[3 ,('nome_acao')] == 'null'
        assert analizar_nome.dataframe.loc[3 ,('nome_bet')] == 'null'
        assert analizar_nome.dataframe.loc[3 ,('nome_jogada')] == 'null'
        assert analizar_nome.dataframe.loc[3 ,('nome_utima_bet')] == 'OR'
        assert analizar_nome.dataframe.loc[3 ,('nome_vilao')] == 'UTG'

        self.incrementar_dataframe(dataframe ,4)
        analizar_nome.analizar(4)
        assert analizar_nome.dataframe.loc[4 ,('nome_acao')] == 'RAISE'
        assert analizar_nome.dataframe.loc[4 ,('nome_bet')] == '3BET'
        assert analizar_nome.dataframe.loc[4 ,('nome_jogada')] == 'ALL IN'
        assert analizar_nome.dataframe.loc[4 ,('nome_utima_bet')] == '3BET'
        assert analizar_nome.dataframe.loc[4 ,('nome_vilao')] == 'CO'

        self.incrementar_dataframe(dataframe ,5)
        analizar_nome.analizar(5)
        assert analizar_nome.dataframe.loc[5 ,('nome_acao')] == 'CHECK'
        assert analizar_nome.dataframe.loc[5 ,('nome_bet')] == 'null'
        assert analizar_nome.dataframe.loc[5 ,('nome_jogada')] == 'null'
        assert analizar_nome.dataframe.loc[5 ,('nome_utima_bet')] == '3BET'
        assert analizar_nome.dataframe.loc[5 ,('nome_vilao')] == 'CO'


    def incrementar_dataframe(self ,dataframe ,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index ,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'mao' :1 ,'bord_etapa' :'FLOP' ,'hole_cards_A' :True,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'SB',
                        'size_bet_vilao' :0 ,'size_bet_fichas' :0.03}
        elif novo_ficheiro == 1:
            ficheiro = {'mao' :1 ,'bord_etapa' :'FLOP' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'BB',
                        'size_bet_vilao' :1 ,'size_bet_fichas' :0.03}
        elif novo_ficheiro == 2:
            ficheiro = {'mao' :1 ,'bord_etapa' :'FLOP' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'UTG',
                        'size_bet_vilao' :2 ,'size_bet_fichas' :0.03}
        elif novo_ficheiro == 3:
            ficheiro = {'mao' :1 ,'bord_etapa' :'FLOP' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'null' ,'ultimo_jogador_posicao' :'MP',
                        'size_bet_vilao' :2 ,'size_bet_fichas' :0.03}
        elif novo_ficheiro == 4:
            ficheiro = {'mao' :1 ,'bord_etapa' :'FLOP' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'CO',
                        'size_bet_vilao' :2 ,'size_bet_fichas' :1}
        elif novo_ficheiro == 5:
            ficheiro = {'mao' :1 ,'bord_etapa' :'FLOP' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'BTN',
                        'size_bet_vilao' :0 ,'size_bet_fichas' :0.03}
        elif novo_ficheiro == 6:
            ficheiro = {'mao' :1 ,'bord_etapa' :'FLOP' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'SB',
                        'size_bet_vilao' :0 ,'size_bet_fichas' :0.03}
        elif novo_ficheiro == 7:
            ficheiro = {'mao' :1 ,'bord_etapa' :'TURN' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'BB',
                        'size_bet_vilao' :1 ,'size_bet_fichas' :0.03}
        elif novo_ficheiro == 8:
            ficheiro = {'mao' :1 ,'bord_etapa' :'TURN' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'UTG',
                        'size_bet_vilao' :2 ,'size_bet_fichas' :1}
        elif novo_ficheiro == 9:
            ficheiro = {'mao' :1 ,'bord_etapa' :'TURN' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'MP',
                        'size_bet_vilao' :2 ,'size_bet_fichas' :1}
        elif novo_ficheiro == 10:
            ficheiro = {'mao' :1 ,'bord_etapa' :'TURN' ,'hole_cards_A' :False,'tela':1,'linha':'null',
                        'ultimo_jogador_letra' :'A' ,'ultimo_jogador_posicao' :'CO',
                        'size_bet_vilao' :1 ,'size_bet_fichas' :0.03}


        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Analista_ultimo_jogador')
    unittest.main()
