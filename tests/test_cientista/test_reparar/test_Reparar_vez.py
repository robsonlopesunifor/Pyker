import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_vez as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Reparar_vez_test(unittest.TestCase,Auxiliar):

    def test_repara(self):
        print('------------ validar -----------------')
        reparar_vez = Reparar.Reparar_vez()
        dataframe = pd.DataFrame()
        reparar_vez.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        self.reparar_dicionario_com_telas_embaralhadas(dataframe, reparar_vez, 4, 3)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'valido_vez_A' :True ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}
        elif novo_ficheiro == 1:
            ficheiro = {'valido_vez_A' :True ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}
        elif novo_ficheiro == 2:
            ficheiro = {'valido_vez_A' :True ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}
        elif novo_ficheiro == 3:
            ficheiro = {'valido_vez_A' :True ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}
        return ficheiro

if __name__ == "__main__":
    print('Teste da classe Regra pote rodada')
    unittest.main()
