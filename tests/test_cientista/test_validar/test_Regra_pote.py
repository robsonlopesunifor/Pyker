import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_pote

class Regra_pote_test(unittest.TestCase,Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar ---------------')
        regra_pote = Regra_pote.Regra_pote()
        dataframe = pd.DataFrame()
        regra_pote.iniciar(dataframe, ['A', 'B', 'C', 'D', 'E', 'F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(10, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_pote.validar(idx)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

        dataframe = regra_pote.dataframe[regra_pote.dataframe['tela'] == 1].reset_index()

        self.assertEqual(dataframe.loc[0, ('valido_pote')], False)
        self.assertEqual(dataframe.loc[1, ('valido_pote')], True)
        self.assertEqual(dataframe.loc[2, ('valido_pote')], False)
        self.assertEqual(dataframe.loc[3, ('valido_pote')], True)
        self.assertEqual(dataframe.loc[4, ('valido_pote')], False)
        self.assertEqual(dataframe.loc[5, ('valido_pote')], False)
        self.assertEqual(dataframe.loc[6, ('valido_pote')], True)
        self.assertEqual(dataframe.loc[7, ('valido_pote')], True)
        self.assertEqual(dataframe.loc[8, ('valido_pote')], False)
        self.assertEqual(dataframe.loc[9, ('valido_pote')], False)


    def gerador_de_ficheiros(self, novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote_rodada': 2.00, 'pote': 0.00, 'mao': 20,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 1:
            ficheiro = {'pote_rodada': 2.00, 'pote': 3.00, 'mao': 20,
                        'aposta_A': 1.00, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 2:
            ficheiro = {'pote_rodada': 2.00, 'pote': 0.00, 'mao': 21,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 3:
            ficheiro = {'pote_rodada': 3.00, 'pote': 3.00, 'mao': 21,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 4:
            ficheiro = {'pote_rodada': 2.00, 'pote': 3.00, 'mao': 21,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 5:
            ficheiro = {'pote_rodada': 2.00, 'pote': 5.00, 'mao': 21,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 6:
            ficheiro = {'pote_rodada': 2.00, 'pote': 2.00, 'mao': 22,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 7:
            ficheiro = {'pote_rodada': 2.00, 'pote': 2.00, 'mao': 22,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 8:
            ficheiro = {'pote_rodada': 2.00, 'pote': 5.00, 'mao': 22,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        elif novo_ficheiro == 9:
            ficheiro = {'pote_rodada': 2.00, 'pote': 6.00, 'mao': 22,
                        'aposta_A': 0, 'aposta_B': 0, 'aposta_C': 0, 'aposta_D': 0, 'aposta_E': 0, 'aposta_F': 0}
        return ficheiro


if __name__ == "__main__":
    print('Teste da classe Regra pote')
    unittest.main()
