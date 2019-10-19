import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_pote_rodada

class Regra_pote_rodada_test(unittest.TestCase,Funcoes_Axiliares):

    def test_validar(self):
        print('------------ validar -----------------')
        regra_pote_rodada = Regra_pote_rodada.Regra_pote_rodada()
        dataframe_pote_rodada = pd.DataFrame()
        regra_pote_rodada.iniciar(dataframe_pote_rodada ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(10, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe_pote_rodada.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe_pote_rodada.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_pote_rodada.validar(idx)

        tela_1 = regra_pote_rodada.dataframe[regra_pote_rodada.dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = regra_pote_rodada.dataframe[regra_pote_rodada.dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = regra_pote_rodada.dataframe[regra_pote_rodada.dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)


    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :0.00 ,'mao' :1,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 1:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :3.00 ,'mao' :1,
                        'aposta_A' :0 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 2:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :3.00 ,'mao' :1,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 3:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :0.00 ,'mao' :1,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 4:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :2.00 ,'mao' :1,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 5:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :3.00 ,'mao' :1,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :2 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 6:
            ficheiro = {'pote_rodada' :3.00 ,'pote' :3.00 ,'mao' :1,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 7:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :5.00 ,'mao' :1,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :'C2'
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 8:
            ficheiro = {'pote_rodada' :0.00 ,'pote' :5.00 ,'mao' :1,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :2 ,'aposta_E' :1 ,'aposta_F' :0,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        elif novo_ficheiro == 9:
            ficheiro = {'pote_rodada' :5.00 ,'pote' :5.00 ,'mao' :1,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :2 ,'aposta_E' :1 ,'aposta_F' :3,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :''
                        ,'bord_RIVER' :''}
        return ficheiro



if __name__ == "__main__":
    print('Teste da classe Regra pote rodada')
    unittest.main()
