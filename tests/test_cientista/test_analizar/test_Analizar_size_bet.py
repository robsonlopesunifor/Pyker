import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Analizar.Analizar_size_bet as Analizar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Analizar_size_bet_test(unittest.TestCase,Auxiliar):

    def test_analizar(self):
        analizar_size_bet = Analizar.Analizar_size_bet()
        dataframe = pd.DataFrame()
        analizar_size_bet.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])

        self.incrementar_dataframe(dataframe ,0)
        analizar_size_bet.analizar(0)
        assert analizar_size_bet.dataframe.loc[0 ,('size_bet_valor')] == 1.1
        assert analizar_size_bet.dataframe.loc[0 ,('size_bet_blind')] == 1

        self.incrementar_dataframe(dataframe, 1)
        analizar_size_bet.analizar(1)
        assert analizar_size_bet.dataframe.loc[1 ,('size_bet_valor')] == 2.2
        assert analizar_size_bet.dataframe.loc[1 ,('size_bet_blind')] == 2
        assert analizar_size_bet.dataframe.loc[1 ,('size_bet_pote')] == 0.5
        assert analizar_size_bet.dataframe.loc[1 ,('size_bet_vilao')] == 2.0
        assert analizar_size_bet.dataframe.loc[1 ,('size_bet_fichas')] == 0.11

        self.incrementar_dataframe(dataframe, 2)
        analizar_size_bet.analizar(2)
        assert analizar_size_bet.dataframe.loc[2 ,('size_bet_valor')] == 2.2
        assert analizar_size_bet.dataframe.loc[2 ,('size_bet_blind')] == 2.0
        assert analizar_size_bet.dataframe.loc[2 ,('size_bet_pote')] == 0.2
        assert analizar_size_bet.dataframe.loc[2 ,('size_bet_vilao')] == 1.0
        assert analizar_size_bet.dataframe.loc[2 ,('size_bet_fichas')] == 0.11

        self.incrementar_dataframe(dataframe, 3)
        analizar_size_bet.analizar(3)
        assert analizar_size_bet.dataframe.loc[3 ,('size_bet_valor')] == 6.2
        assert analizar_size_bet.dataframe.loc[3 ,('size_bet_blind')] == 5.64
        assert analizar_size_bet.dataframe.loc[3 ,('size_bet_pote')] == 0.56
        assert analizar_size_bet.dataframe.loc[3 ,('size_bet_vilao')] == 2.82
        assert analizar_size_bet.dataframe.loc[3 ,('size_bet_fichas')] == 0.31
        """
        self.incrementar_dataframe(dataframe,4)
        analizar_size_bet.analizar(4)
        assert analizar_size_bet.dataframe.loc[4,('ultimo_jogador_posicao')] == 'SB'  

        self.incrementar_dataframe(dataframe,5)
        analizar_size_bet.analizar(5)
        assert analizar_size_bet.dataframe.loc[5,('ultimo_jogador_posicao')] == 'null'
        """

    def incrementar_dataframe(self ,dataframe ,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index ,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'mao' :1 ,'ultimo_jogador_letra' :'A' ,'hole_cards_A' :False ,'aposta_A' :1.1 ,'fichas_B' :10.0
                        ,'aposta_B' :1.1 ,'aposta_C' :1.1 ,'pote' :2.2,'tela':1,
                        'linha' :'normal' ,'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False
                        ,'diler_E' :False ,'diler_F' :False}
        elif novo_ficheiro == 1:
            ficheiro = {'mao' :1 ,'ultimo_jogador_letra' :'B' ,'hole_cards_B' :False ,'aposta_B' :2.2 ,'fichas_C' :10.0
                        ,'aposta_C' :1.1 ,'pote' :5.5,'tela':1,
                        'linha' :'normal' ,'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False
                        ,'diler_E' :False ,'diler_F' :False}
        elif novo_ficheiro == 2:
            ficheiro = {'mao' :1 ,'ultimo_jogador_letra' :'C' ,'hole_cards_C' :False ,'aposta_C' :2.2 ,'fichas_D' :10.0
                        ,'aposta_D' :3.1 ,'pote' :5.5,'tela':1,
                        'linha' :'normal' ,'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False
                        ,'diler_E' :False ,'diler_F' :False}
        elif novo_ficheiro == 3:
            ficheiro = {'mao' :1 ,'ultimo_jogador_letra' :'D' ,'hole_cards_D' :False ,'aposta_C' :1.1 ,'aposta_D' :6.2
                        ,'fichas_E' :10.0 ,'aposta_E' :5.4 ,'pote' :5.5,'tela':1,
                        'linha' :'normal' ,'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False
                        ,'diler_E' :False ,'diler_F' :False}
        elif novo_ficheiro == 4:
            ficheiro = {'mao' :2 ,'ultimo_jogador_letra' :'E' ,'hole_cards_E' :False ,'aposta_C' :1.1 ,'aposta_E' :5.4
                        ,'fichas_F' :10.0 ,'aposta_F' :0 ,'pote' :5.5,'tela':1,
                        'linha' :'normal' ,'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False
                        ,'diler_E' :False ,'diler_F' :False}
        elif novo_ficheiro == 5:
            ficheiro = {'mao' :2 ,'ultimo_jogador_letra' :'F' ,'hole_cards_F' :False ,'aposta_C' :1.1 ,'aposta_F' :0
                        ,'fichas_A' :10.0 ,'aposta_A' :5.2 ,'pote' :5.5,'tela':1,
                        'linha' :'normal' ,'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False
                        ,'diler_E' :False ,'diler_F' :False}
        elif novo_ficheiro == 6:
            ficheiro = {'linha' :'normal' ,'mao' :1 ,'ultimo_jogador_letra' :'A' ,'hole_cards_A' :False
                        ,'aposta_C' :1.1 ,'aposta_A' :15.6 ,'pote' :5.5}
        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Analista_ultimo_jogador')
    unittest.main()
