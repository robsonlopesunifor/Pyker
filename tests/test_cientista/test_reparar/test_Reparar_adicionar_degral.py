import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_adicionar_degral as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar



class Reparar_adicionar_degral_test(unittest.TestCase,Auxiliar):

    def test_repara(self):
        print('------------ validar -----------------')
        reparar_adicionar_degral = Reparar.Reparar_adicionar_degral()
        dataframe = pd.DataFrame()
        reparar_adicionar_degral.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        self.reparar_dicionario_com_telas_embaralhadas(dataframe,reparar_adicionar_degral,5,3)
        print(reparar_adicionar_degral.dataframe)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)


    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote' :0.45 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 1:
            ficheiro = {'pote' :0.75 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :True
                        ,'hole_cards_E' :True ,'hole_cards_F' :True}
        elif novo_ficheiro == 2:
            ficheiro = {'pote' :0.45 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :True
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 3:
            ficheiro = {'pote' :0.75 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :True
                        ,'hole_cards_E' :True ,'hole_cards_F' :True}
        elif novo_ficheiro == 4:
            ficheiro = {'pote' :0.75 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'hole_cards_A' :True ,'hole_cards_B' :True ,'hole_cards_C' :True ,'hole_cards_D' :True
                        ,'hole_cards_E' :True ,'hole_cards_F' :True}

        return ficheiro

if __name__ == "__main__":
    print('Teste da classe Reparar_adicionar_degral')
    unittest.main()
