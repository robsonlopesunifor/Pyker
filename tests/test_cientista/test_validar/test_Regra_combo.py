import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_combo

class Regra_combo_test(unittest.TestCase,Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar -----------------')
        combo = Regra_combo.Regra_combo()
        dataframe_combo = pd.DataFrame()
        combo.iniciar(dataframe_combo,['A','B','C','D','E','F'])
        for x in range(0,5):
            dataframe_combo.loc[x] = False
            novo_ficheiro = self.gerador_de_ficheiros(x)
            for chave in novo_ficheiro:
                dataframe_combo.loc[x,(chave)] = novo_ficheiro[chave]
            #regra_combo.validar(x)
        print(combo.dataframe)

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'combo_A_1':'C2','combo_B_1':'','combo_C_1':'',
                        'combo_E_1':'', 'combo_D_1': 'C2', 'combo_F_1': '',
                        'combo_A_2':'C2','combo_B_2':'','combo_C_2':'',
                        'combo_E_2': '', 'combo_D_2': 'C2', 'combo_F_2': ''}
        elif novo_ficheiro == 1:
            ficheiro = {'combo_A_1':'C2','combo_B_1':'','combo_C_1':'',
                        'combo_E_1':'', 'combo_D_1': 'C2', 'combo_F_1': '',
                        'combo_A_2':'C2','combo_B_2':'','combo_C_2':'',
                        'combo_E_2': '', 'combo_D_2': 'C2', 'combo_F_2': ''}
        elif novo_ficheiro == 2:
            ficheiro = {'combo_A_1':'C2','combo_B_1':'','combo_C_1':'',
                        'combo_E_1':'', 'combo_D_1': 'C2', 'combo_F_1': '',
                        'combo_A_2':'C2','combo_B_2':'','combo_C_2':'',
                        'combo_E_2': '', 'combo_D_2': 'C2', 'combo_F_2': ''}
        elif novo_ficheiro == 3:
            ficheiro = {'combo_A_1':'C2','combo_B_1':'','combo_C_1':'',
                        'combo_E_1':'', 'combo_D_1': 'C2', 'combo_F_1': '',
                        'combo_A_2':'C2','combo_B_2':'','combo_C_2':'',
                        'combo_E_2': '', 'combo_D_2': 'C2', 'combo_F_2': ''}
        elif novo_ficheiro == 4:
            ficheiro = {'combo_A_1':'C2','combo_B_1':'','combo_C_1':'',
                        'combo_E_1':'', 'combo_D_1': 'C2', 'combo_F_1': '',
                        'combo_A_2':'C2','combo_B_2':'','combo_C_2':'',
                        'combo_E_2': '', 'combo_D_2': 'C2', 'combo_F_2': ''}
        elif novo_ficheiro == 5:
            ficheiro = {'combo_A_1':'C2','combo_B_1':'','combo_C_1':'',
                        'combo_E_1':'', 'combo_D_1': 'C2', 'combo_F_1': '',
                        'combo_A_2':'C2','combo_B_2':'','combo_C_2':'',
                        'combo_E_2': '', 'combo_D_2': 'C2', 'combo_F_2': ''}
        return ficheiro

if __name__ == "__main__":
    print('Teste da classe Regra hole cards')
    unittest.main()
