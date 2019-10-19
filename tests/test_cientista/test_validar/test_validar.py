import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Validar as Validar

class Validador_Test(unittest.TestCase):


    def test_iniciar(self):
        print('------------- test_iniciar ---------------')
        validador = Validar.Validador()
        dataframe_valido = pd.DataFrame()
        validador.iniciar(dataframe_valido)

    def test_validar(self):
        print('------------- adicionar_ficheiro_a_tabela ---------------')
        validador = Validar.Validador()
        self.dataframe = pd.read_csv('datagrama.csv', sep=';')
        validador.iniciar(self.dataframe)
        for x in range(1, 20):
            validador.validar(x)
        print(validador.dataframe_valido['valido_pote'])


if __name__ == "__main__":
    print('____Teste da classe Validar Fiheiro')
    unittest.main()