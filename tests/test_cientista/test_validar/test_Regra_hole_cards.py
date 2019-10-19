import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_hole_cards


class Regra_hole_cards_test(unittest.TestCase,Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar -----------------')
        regra_hole_cards = Regra_hole_cards.Regra_hole_cards()
        dataframe_hole_cards = pd.DataFrame()
        regra_hole_cards.iniciar(dataframe_hole_cards,['A','B','C','D','E','F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(6, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe_hole_cards.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe_hole_cards.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_hole_cards.validar(idx)


        tela_1 = dataframe_hole_cards[dataframe_hole_cards['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe_hole_cards[dataframe_hole_cards['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe_hole_cards[dataframe_hole_cards['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 1:
            ficheiro = {'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 2:
            ficheiro = {'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 3:
            ficheiro = {'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 4:
            ficheiro = {'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 5:
            ficheiro = {'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        return ficheiro


if __name__ == "__main__":
    print('Teste da classe Regra hole cards')
    unittest.main()
