import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_vez

class Regra_vez_test(unittest.TestCase,Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar -----------------')
        regra_vez = Regra_vez.Regra_vez()
        dataframe = pd.DataFrame()
        regra_vez.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(4, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_vez.validar(idx)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)


    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'hole_cards_A' :False ,'hole_cards_B' :True ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'valido_vez_A' :True ,'valido_vez_B' :True ,'valido_vez_C' :True ,'valido_vez_D' :True
                        ,'valido_vez_E' :True ,'valido_vez_F' :True}
        elif novo_ficheiro == 1:
            ficheiro = {'hole_cards_A' :False ,'hole_cards_B' :True ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False,
                        'vez_A' :True ,'vez_B' :True ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'valido_vez_A' :False ,'valido_vez_B' :True ,'valido_vez_C' :True ,'valido_vez_D' :True
                        ,'valido_vez_E' :True ,'valido_vez_F' :True}
        elif novo_ficheiro == 2:
            ficheiro = {'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :True ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False,
                        'vez_A' :False ,'vez_B' :True ,'vez_C' :False ,'vez_D' :True ,'vez_E' :False ,'vez_F' :False,
                        'valido_vez_A' :False ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}
        elif novo_ficheiro == 3:
            ficheiro = {'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :True ,'vez_D' :True ,'vez_E' :True ,'vez_F' :False,
                        'valido_vez_A' :False ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}
        elif novo_ficheiro == 4:
            ficheiro = {'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :True,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :True ,'vez_D' :True ,'vez_E' :False ,'vez_F' :True,
                        'valido_vez_A' :False ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}
        elif novo_ficheiro == 5:
            ficheiro = {'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :True ,'vez_D' :True ,'vez_E' :True ,'vez_F' :False,
                        'valido_vez_A' :False ,'valido_vez_B' :False ,'valido_vez_C' :False ,'valido_vez_D' :False
                        ,'valido_vez_E' :False ,'valido_vez_F' :False}

        return ficheiro


if __name__ == "__main__":
    print('Teste da classe Regra vez')
    unittest.main()
