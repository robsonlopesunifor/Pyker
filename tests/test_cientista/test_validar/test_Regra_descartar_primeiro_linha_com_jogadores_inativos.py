import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_descartar_primeira_linha_com_jogadores_inativos

class Regra_descartar_primeira_linha_com_jogadores_inativos_test(unittest.TestCase,Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar -----------------')
        regra_descartar_primeira_linha_com_jogadores_inativos = Regra_descartar_primeira_linha_com_jogadores_inativos.Regra_descartar_primeira_linha_com_jogadores_inativos()
        dataframe = pd.DataFrame()
        regra_descartar_primeira_linha_com_jogadores_inativos.iniciar(dataframe,['A','B','C','D','E','F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(6, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_descartar_primeira_linha_com_jogadores_inativos.validar(idx)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'bord_etapa':'RIVER','mao':1,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 1:
            ficheiro = {'bord_etapa':'RIVER','mao':1,'hole_cards_A':False,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 2:
            ficheiro = {'bord_etapa':'RIVER','mao':1,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 3:
            ficheiro = {'bord_etapa':'RIVER','mao':2,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 4:
            ficheiro = {'bord_etapa':'RIVER','mao':2,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 5:
            ficheiro = {'bord_etapa':'RIVER','mao':2,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        return ficheiro


if __name__ == "__main__":
    print('Teste da classe Regra_descartar_linha_com_jogadores_inativos')
    unittest.main()
