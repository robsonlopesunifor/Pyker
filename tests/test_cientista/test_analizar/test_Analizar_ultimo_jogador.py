import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Analizar.Analizar_ultimo_jogador as Analizar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Analizar_ultimo_jogador_test(unittest.TestCase,Auxiliar):

    def test_ultimo_jogador(self):
        pass

    def test_analizar(self):
        analizar_ultimo_jogador = Analizar.Analizar_ultimo_jogador()
        dataframe = pd.DataFrame()
        analizar_ultimo_jogador.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])

        self.incrementar_dataframe(dataframe ,0)
        analizar_ultimo_jogador.analizar(0)
        assert analizar_ultimo_jogador.dataframe.loc[0 ,('ultimo_jogador_posicao')] == 'BB'

        self.incrementar_dataframe(dataframe ,1)
        analizar_ultimo_jogador.analizar(1)
        assert analizar_ultimo_jogador.dataframe.loc[1 ,('ultimo_jogador_posicao')] == 'UTG'

        self.incrementar_dataframe(dataframe ,2)
        analizar_ultimo_jogador.analizar(2)
        assert analizar_ultimo_jogador.dataframe.loc[2 ,('ultimo_jogador_posicao')] == 'MP'

        self.incrementar_dataframe(dataframe ,3)
        analizar_ultimo_jogador.analizar(3)
        assert analizar_ultimo_jogador.dataframe.loc[3 ,('ultimo_jogador_posicao')] == 'BTN'

        self.incrementar_dataframe(dataframe ,4)
        analizar_ultimo_jogador.analizar(4)
        assert analizar_ultimo_jogador.dataframe.loc[4 ,('ultimo_jogador_posicao')] == 'SB'

        self.incrementar_dataframe(dataframe ,5)
        analizar_ultimo_jogador.analizar(5)
        assert analizar_ultimo_jogador.dataframe.loc[5 ,('ultimo_jogador_posicao')] == 'null'


    def incrementar_dataframe(self ,dataframe ,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index ,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'bord_etapa' :'RIVER' ,'linha' :'normal' ,'mao' :1,'tela':1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :True ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 1:
            ficheiro = {'bord_etapa' :'RIVER' ,'linha' :'normal' ,'mao' :1,'tela':1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :True ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 2:
            ficheiro = {'bord_etapa' :'RIVER' ,'linha' :'normal' ,'mao' :1,'tela':1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 3:
            ficheiro = {'bord_etapa' :'RIVER' ,'linha' :'normal' ,'mao' :1,'tela':1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :False ,'vez_B' :True ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 4:
            ficheiro = {'bord_etapa' :'RIVER' ,'linha' :'normal' ,'mao' :1,'tela':1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 5:
            ficheiro = {'bord_etapa' :'RIVER' ,'linha' :'normal' ,'mao' :1,'tela':1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 6:
            ficheiro = {'bord_etapa' :'RIVER' ,'linha' :'normal' ,'mao' :1,'tela':1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Analista_ultimo_jogador')
    unittest.main()
