import unittest
import pandas as pd
import numpy as np
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_hole_cards as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Reparar_hole_cards_test(unittest.TestCase,Auxiliar):

    def test_validar(self):
        print('------------ validar -----------------')
        reparar_hole_cards = Reparar.Reparar_hole_cards()
        dataframe = pd.DataFrame()
        reparar_hole_cards.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        self.reparar_dicionario_com_telas_embaralhadas(dataframe,reparar_hole_cards,3,3)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

        print(reparar_hole_cards.dataframe.loc[:, ('hole_cards_A',
                                                   'hole_cards_B',
                                                   'hole_cards_C',
                                                   'hole_cards_D',
                                                   'hole_cards_E',
                                                   'hole_cards_F')])


    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :True ,'hole_cards_E': False, 'hole_cards_D': False, 'hole_cards_F': False,
                        'combo_A_1' :'C' ,'combo_A_2' :'K' ,'combo_B_1' :np.nan ,'combo_B_2' :np.nan ,'combo_C_1' :'P'
                        ,'combo_C_2' :'9',
                        'combo_D_1' :np.nan ,'combo_D_2' :np.nan ,'combo_E_1' :np.nan ,'combo_E_2' :np.nan
                        ,'combo_F_1' :np.nan ,'combo_F_2' :np.nan}

        elif novo_ficheiro == 1:
            ficheiro = {'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :True ,'hole_cards_E': False, 'hole_cards_D': False, 'hole_cards_F': False,
                        'combo_A_1' :'C' ,'combo_A_2' :'K' ,'combo_B_1' :np.nan ,'combo_B_2' :np.nan ,'combo_C_1' :'P'
                        ,'combo_C_2' :'9',
                        'combo_D_1' :np.nan ,'combo_D_2' :np.nan ,'combo_E_1' :np.nan ,'combo_E_2' :np.nan
                        ,'combo_F_1' :np.nan ,'combo_F_2' :np.nan}

        elif novo_ficheiro == 2:
            ficheiro = {'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :True ,'hole_cards_E': False, 'hole_cards_D': False, 'hole_cards_F': False,
                        'combo_A_1' :'C' ,'combo_A_2' :'K' ,'combo_B_1' :np.nan ,'combo_B_2' :np.nan ,'combo_C_1' :'P'
                        ,'combo_C_2' :'9',
                        'combo_D_1' :np.nan ,'combo_D_2' :np.nan ,'combo_E_1' :np.nan ,'combo_E_2' :np.nan
                        ,'combo_F_1' :np.nan ,'combo_F_2' :np.nan}

        return ficheiro

if __name__ == "__main__":
    print('Teste da classe Regra hole cards')
    unittest.main()