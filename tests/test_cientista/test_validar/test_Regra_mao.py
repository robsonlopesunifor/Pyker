import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_mao


class Regra_mao_test(unittest.TestCase,Funcoes_Axiliares):

    def test_definir_mao(self):
        print('------------ validar --------------'
              ' Se o pote atual for menor que o pote anterior \n '
              'e for preflop é nova mão '
              '-----------------------------------')
        regra_mao = Regra_mao.Regra_mao()
        dataframe_pote = pd.DataFrame()
        regra_mao.iniciar(dataframe_pote)
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(10, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe_pote.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe_pote.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_mao.definir_mao(idx)

        tela_1 = regra_mao.dataframe[regra_mao.dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = regra_mao.dataframe[regra_mao.dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = regra_mao.dataframe[regra_mao.dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        print(tela_1)
        print(tela_2)
        print(tela_3)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

        dataframe = regra_mao.dataframe[regra_mao.dataframe['tela'] == 1].reset_index()

        self.assertEqual( dataframe.loc[0, ('mao')], 1)
        self.assertEqual( dataframe.loc[1, ('mao')], 1)
        self.assertEqual( dataframe.loc[2, ('mao')], 2)
        self.assertEqual( dataframe.loc[3, ('mao')], 2)
        self.assertEqual( dataframe.loc[4, ('mao')], 2)
        self.assertEqual( dataframe.loc[5, ('mao')], 2)
        self.assertEqual( dataframe.loc[6, ('mao')], 3)
        self.assertEqual( dataframe.loc[7, ('mao')], 3)
        self.assertEqual( dataframe.loc[8, ('mao')], 3)
        self.assertEqual( dataframe.loc[9, ('mao')], 3)


    def gerador_de_ficheiros(self, novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote': 0.00, 'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 1:
            ficheiro = {'pote': 3.00, 'bord_FLOP_1': 'C4', 'bord_FLOP_2': '2C', 'bord_FLOP_3': '2C', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 2:
            ficheiro = {'pote': 0.00, 'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 3:
            ficheiro = {'pote': 3.00, 'bord_FLOP_1': '2C', 'bord_FLOP_2': '2c', 'bord_FLOP_3': '2C', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 4:
            ficheiro = {'pote': 0.00, 'bord_FLOP_1': '2C', 'bord_FLOP_2': '2c', 'bord_FLOP_3': '2C', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 5:
            ficheiro = {'pote': 5.00, 'bord_FLOP_1': '2C', 'bord_FLOP_2': '2c', 'bord_FLOP_3': '2C', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 6:
            ficheiro = {'pote': 2.00, 'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 7:
            ficheiro = {'pote': 2.00, 'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 8:
            ficheiro = {'pote': 5.00, 'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '',
                        'bord_TURN': ''}
        elif novo_ficheiro == 9:
            ficheiro = {'pote': 6.00, 'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '',
                        'bord_TURN': ''}
        return ficheiro



if __name__ == "__main__":
    print('Teste da classe Regra mao')
    unittest.main()