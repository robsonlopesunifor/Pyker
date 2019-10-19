import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Analizar.Analizar_showdown as Analizar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Analizar_showdown_test(unittest.TestCase,Auxiliar):

    def test_analizar(self):
        analizar_showdown = Analizar.Analizar_showdown()
        dataframe = pd.DataFrame()
        analizar_showdown.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        self.analizar_dicionario_com_telas_embaralhadas(dataframe,analizar_showdown,8,3)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

    def incrementar_dataframe(self ,dataframe ,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index ,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'mao' :1 ,'combo_A_1' :'' ,'combo_B_1' :'9s9c' ,'combo_C_1' :'' ,'combo_D_1' :''
                        ,'combo_E_1' :'' ,'combo_F_1' :''}
        elif novo_ficheiro == 1:
            ficheiro = {'mao' :1 ,'combo_A_1' :'' ,'combo_B_1' :'9s9c' ,'combo_C_1' :'' ,'combo_D_1' :''
                        ,'combo_E_1' :'' ,'combo_F_1' :''}
        elif novo_ficheiro == 2:
            ficheiro = {'mao' :1 ,'combo_A_1' :'' ,'combo_B_1' :'9s9c' ,'combo_C_1' :'9s9c' ,'combo_D_1' :''
                        ,'combo_E_1' :'' ,'combo_F_1' :''}
        elif novo_ficheiro == 3:
            ficheiro = {'mao' :1 ,'combo_A_1' :'9s9c' ,'combo_B_1' :'9s9c' ,'combo_C_1' :'' ,'combo_D_1' :'9s9c'
                        ,'combo_E_1' :'' ,'combo_F_1' :''}
        elif novo_ficheiro == 4:
            ficheiro = {'mao' :2 ,'combo_A_1' :'' ,'combo_B_1' :'' ,'combo_C_1' :'' ,'combo_D_1' :'' ,'combo_E_1' :''
                        ,'combo_F_1' :''}
        elif novo_ficheiro == 5:
            ficheiro = {'mao' :2 ,'combo_A_1' :'9s9c' ,'combo_B_1' :'' ,'combo_C_1' :'' ,'combo_D_1' :''
                        ,'combo_E_1' :'' ,'combo_F_1' :''}
        elif novo_ficheiro == 6:
            ficheiro = {'mao' :2 ,'combo_A_1' :'9s9c' ,'combo_B_1' :'9s9c' ,'combo_C_1' :'' ,'combo_D_1' :''
                        ,'combo_E_1' :'' ,'combo_F_1' :''}
        elif novo_ficheiro == 7:
            ficheiro = {'mao' :2 ,'combo_A_1' :'9s9c' ,'combo_B_1' :'9s9c' ,'combo_C_1' :'9s9c' ,'combo_D_1' :''
                        ,'combo_E_1' :'' ,'combo_F_1' :''}

        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Analista_heroi')
    unittest.main()
