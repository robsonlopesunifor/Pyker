import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_adicionar_linha as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Reparar_adicionar_linha_test(unittest.TestCase,Auxiliar):

    def test_repara(self):
        print('------------ validar -----------------')
        reparar_adicionar_linha = Reparar.Reparar_adicionar_linha()
        dataframe = pd.DataFrame()
        reparar_adicionar_linha.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        self.reparar_dicionario_com_telas_embaralhadas(dataframe, reparar_adicionar_linha, 4, 3)

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
                        'aposta_A' :0 ,'aposta_B' :0.05 ,'aposta_C' :0.1 ,'aposta_D' :0.3 ,'aposta_E' :0 ,'aposta_F' :0,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :True ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 1:
            ficheiro = {'pote' :0.75 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'aposta_A' :0 ,'aposta_B' :0.05 ,'aposta_C' :0.1 ,'aposta_D' :0.3 ,'aposta_E' :0.3
                        ,'aposta_F' :0,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :True}
        elif novo_ficheiro == 2:
            ficheiro = {'pote' :0.75 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'aposta_A' :0 ,'aposta_B' :0.1 ,'aposta_C' :0.3 ,'aposta_D' :0.3 ,'aposta_E' :0.3
                        ,'aposta_F' :0,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :True}
        elif novo_ficheiro == 3:
            ficheiro = {'pote' :4.04 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'aposta_A' :0 ,'aposta_B' :0.1 ,'aposta_C' :0.3 ,'aposta_D' :0.3 ,'aposta_E' :0.3
                        ,'aposta_F' :0,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :True ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :True ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :True}
        return ficheiro



if __name__ == "__main__":
    print('Teste da classe Regra pote rodada')
    unittest.main()
