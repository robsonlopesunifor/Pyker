import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Analizar as Analizar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Analizar_Test(unittest.TestCase,Auxiliar):

    def test_iniciar(self):
        analizar = Analizar.Analizar()
        dataframe = pd.DataFrame()
        analizar.iniciar(dataframe)

    def test_analizar(self):
        print('------------- adicionar_ficheiro_a_tabela ---------------')
        analizar = Analizar.Analizar()
        dataframe = self.embaralhar_dataframe('dataframe.csv', 3)
        analizar.iniciar(dataframe)
        for x in range(len(dataframe)):
            analizar.analizar(x)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)


if __name__ == "__main__":
    print('____Teste da classe Analizar ficheiro')
    unittest.main()
