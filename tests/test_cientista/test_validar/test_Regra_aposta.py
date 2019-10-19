import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_aposta


class Regra_aposta_test(unittest.TestCase, Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar -----------------')
        regra_aposta = Regra_aposta.Regra_aposta()
        dataframe_aposta = pd.DataFrame()
        regra_aposta.iniciar(dataframe_aposta ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(8,3)
        for idx,tupla in enumerate(lista_telas_embaralhadas):
            dataframe_aposta.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela',tupla[0])
            for chave in novo_ficheiro:
                dataframe_aposta.loc[idx ,(chave)] = novo_ficheiro[chave]
            regra_aposta.validar(idx)

        tela_1 = regra_aposta.dataframe[regra_aposta.dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = regra_aposta.dataframe[regra_aposta.dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = regra_aposta.dataframe[regra_aposta.dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)


    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :0 ,'fichas_B' :0 ,'fichas_C' :0 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 1:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :5 ,'fichas_B' :5 ,'fichas_C' :5 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 2:
            ficheiro = {'mao' :11,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :4 ,'fichas_B' :4 ,'fichas_C' :4 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 3:
            ficheiro = {'mao' :11,
                        'aposta_A' :2 ,'aposta_B' :2 ,'aposta_C' :2 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :3 ,'fichas_B' :3 ,'fichas_C' :3 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 4:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :3 ,'fichas_B' :3 ,'fichas_C' :3 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 5:
            ficheiro = {'mao' :11,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :2 ,'fichas_B' :2 ,'fichas_C' :2 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 6:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :3 ,'fichas_B' :3 ,'fichas_C' :3 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :'C2'
                        ,'bord_RIVER' :'C2'}
        elif novo_ficheiro == 7:
            ficheiro = {'mao' :11,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :2 ,'fichas_B' :2 ,'fichas_C' :2 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :'C2'
                        ,'bord_RIVER' :'C2'}

        return ficheiro


if __name__ == "__main__":
    print('Teste da classe Regra aposta')
    unittest.main()
