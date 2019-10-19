import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_diler

class Regra_diler_test(unittest.TestCase,Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar -----------------')
        regra_diler = Regra_diler.Regra_diler()
        dataframe_diler = pd.DataFrame()
        regra_diler.iniciar(dataframe_diler, ['A', 'B', 'C', 'D', 'E', 'F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(6, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe_diler.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe_diler.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_diler.validar(idx)

        tela_1 = regra_diler.dataframe[regra_diler.dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = regra_diler.dataframe[regra_diler.dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = regra_diler.dataframe[regra_diler.dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

    def gerador_de_ficheiros(self, novo_ficherio):
        if novo_ficherio == 0:
            ficherio = {'diler_A': True, 'diler_B': False, 'diler_C': False, 'diler_D': False, 'diler_E': False,
                        'diler_F': False}
        elif novo_ficherio == 1:
            ficherio = {'diler_A': True, 'diler_B': False, 'diler_C': False, 'diler_D': False, 'diler_E': False,
                        'diler_F': False}
        elif novo_ficherio == 2:
            ficherio = {'diler_A': True, 'diler_B': False, 'diler_C': False, 'diler_D': False, 'diler_E': False,
                        'diler_F': False}
        elif novo_ficherio == 3:
            ficherio = {'diler_A': True, 'diler_B': False, 'diler_C': False, 'diler_D': False, 'diler_E': False,
                        'diler_F': False}
        elif novo_ficherio == 4:
            ficherio = {'diler_A': True, 'diler_B': False, 'diler_C': False, 'diler_D': False, 'diler_E': False,
                        'diler_F': False}
        elif novo_ficherio == 5:
            ficherio = {'diler_A': True, 'diler_B': False, 'diler_C': False, 'diler_D': False, 'diler_E': False,
                        'diler_F': False}

        return ficherio


if __name__ == "__main__":
    print('Teste da classe Regra diler')
    unittest.main()