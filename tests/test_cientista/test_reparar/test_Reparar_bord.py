import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_bord as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Reparar_bord_test(unittest.TestCase,Auxiliar):


    def test_validar(self):
        print('------------ validar -----------------')
        reparar_bord = Reparar.Reparar_bord()
        dataframe = pd.DataFrame()
        reparar_bord.iniciar(dataframe)
        self.reparar_dicionario_com_telas_embaralhadas(dataframe,reparar_bord,5,3)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)



    def gerador_de_ficheiros(self ,novo_ficheiro):

        if novo_ficheiro == 0:
            ficheiro = {'valido_bord' :True ,'bord_FLOP_1': '2c', 'bord_FLOP_2': '2c', 'bord_FLOP_3': '2c', 'bord_RIVER': '', 'bord_TURN': '' ,'mao' :1}
        elif novo_ficheiro == 1:
            ficheiro = {'valido_bord' :False ,'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '', 'bord_TURN': '' ,'mao' :1}
        elif novo_ficheiro == 2:
            ficheiro = {'valido_bord' :True ,'bord_FLOP_1': '', 'bord_FLOP_2': '', 'bord_FLOP_3': '', 'bord_RIVER': '', 'bord_TURN': '' ,'mao' :1}
        elif novo_ficheiro == 3:
            ficheiro = {'valido_bord' :False ,'bord_FLOP_1': 'C2', 'bord_FLOP_2': 'C2', 'bord_FLOP_3': 'C2', 'bord_RIVER': '', 'bord_TURN': '' ,'mao' :1}
        elif novo_ficheiro == 4:
            ficheiro = {'valido_bord' :True ,'bord_FLOP_1': 'C2', 'bord_FLOP_2': 'C2', 'bord_FLOP_3': 'C2', 'bord_RIVER': '', 'bord_TURN': 'C2' ,'mao' :1}
        return ficheiro

if __name__ == "__main__":
    print('Teste da classe Regra aposta')
    unittest.main()
