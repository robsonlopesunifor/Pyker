import unittest
import json
import sys, os
sys.path.insert(-1,os.path.abspath('../../Pyker'))
import cientista as Cientista
from pyker_sdk.tests.test_cientista.Auxiliar import Auxiliar

class Corretor_ficheiro_Test(unittest.TestCase,Auxiliar):

    def _test_adicionar_com_ficheiros_embaralhado(self):
        print('------------- adicionar_com_ficheiros_embaralhado ---------------')
        cientista = Cientista.Cientista()
        file = open('ficheiro.json')
        ficheiros = json.load(file)
        file.close()
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(len(ficheiros), 3)

        for idx, tupla in enumerate(lista_telas_embaralhadas):
            ficheiro = ficheiros[tupla[1]].copy()
            ficheiro.setdefault('tela', {'A': tupla[0]})
            cientista.adicionar(ficheiro)

        dataframe = cientista.dataframe

        tela_1 = dataframe[dataframe['tela'] == 1].iloc[1:,:].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].iloc[1:,:].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].iloc[1:,:].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

    def test_adicionar_corrigir_com_ficheiros_embaralhado(self):
        print('------------- adicionar_corrigir_com_ficheiros_embaralhado ---------------')
        cientista = Cientista.Cientista()
        file = open('ficheiro.json')
        ficheiros = json.load(file)
        file.close()
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(len(ficheiros), 3)

        for idx, tupla in enumerate(lista_telas_embaralhadas):
            ficheiro = ficheiros[tupla[1]].copy()
            ficheiro.setdefault('tela', {'A': tupla[0]})
            cientista.adicionar_corrigir(ficheiro)

        dataframe = cientista.dataframe

        tela_1 = dataframe[dataframe['tela'] == 1].iloc[1:,:].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].iloc[1:,:].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].iloc[1:,:].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)





if __name__ == "__main__":
    print('____Teste da classe Corretor Fiheiro')
    unittest.main()
