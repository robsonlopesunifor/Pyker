import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista import Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar

class Reparar_ficheiro_Test(unittest.TestCase,Auxiliar):

    def iniciar(self):
        reparar_ficheiro = Reparar.Reparar_ficheiro()
        dataframe_reparado = pd.DataFrame()
        reparar_ficheiro.iniciar(dataframe_reparado)

    def test_reparar(self):
        print('------------- adicionar_ficheiro_a_tabela ---------------')
        reparar = Reparar.Reparar()
        dataframe = self.embaralhar_dataframe('datagrama.csv', 3)
        reparar.iniciar(dataframe)
        for x in range(len(dataframe)):
            reparar.reparar(x)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

        aposta_df = dataframe[(dataframe['valido_aposta_A'] == False) |
                              (dataframe['valido_aposta_B'] == False) |
                              (dataframe['valido_aposta_C'] == False) |
                              (dataframe['valido_aposta_D'] == False) |
                              (dataframe['valido_aposta_E'] == False) |
                              (dataframe['valido_aposta_F'] == False)]

        print('---------- apostas -----------')
        print(aposta_df.loc[:, ('aposta_A', 'aposta_B', 'aposta_C', 'aposta_D', 'aposta_E', 'aposta_F')])

        pote_rodada_df = dataframe[(dataframe['valido_pote_rodada'] == False)]
        print('---------- pote_rodada -----------')
        print(pote_rodada_df.loc[:, ('pote_rodada')])

        bord_df = dataframe[(dataframe['valido_bord'] == False)]
        print('---------- bord -----------')
        print(bord_df.loc[:, ('bord_FLOP_1', 'bord_FLOP_2', 'bord_FLOP_3', 'bord_TURN', 'bord_RIVER')])


if __name__ == "__main__":
    print('____Teste da classe Validar Fiheiro')
    unittest.main()

