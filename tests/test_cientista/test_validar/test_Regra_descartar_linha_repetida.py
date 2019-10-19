import unittest
import pandas as pd
from Funcoes_Axiliares import Funcoes_Axiliares
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
from cientista.Validar import Regra_descartar_linha_repetida

class Regra_descartar_linha_repetida_test(unittest.TestCase,Funcoes_Axiliares):

    def test_repara(self):
        print('------------ validar -----------------')
        regra_descartar_linha_repetida = Regra_descartar_linha_repetida.Regra_descartar_linha_repetida()
        dataframe = pd.DataFrame()
        regra_descartar_linha_repetida.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(4, 3)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe.loc[idx, (chave)] = novo_ficheiro[chave]
            regra_descartar_linha_repetida.validar(idx)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)


    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote' :0.45 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :'C2'
                        ,'bord_RIVER' :'C2',
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'aposta_A' :0 ,'aposta_B' :0.05 ,'aposta_C' :0.1 ,'aposta_D' :0.3 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :0 ,'fichas_B' :0.05 ,'fichas_C' :0.1 ,'fichas_D' :0.3 ,'fichas_E' :0 ,'fichas_F' :0,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :True ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :False}
        elif novo_ficheiro == 1:
            ficheiro = {'pote' :0.75 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :'C2'
                        ,'bord_RIVER' :'C2',
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'aposta_A' :0 ,'aposta_B' :0.05 ,'aposta_C' :0.1 ,'aposta_D' :0.3 ,'aposta_E' :0.3
                        ,'aposta_F' :0,
                        'fichas_A' :0 ,'fichas_B' :0.05 ,'fichas_C' :0.1 ,'fichas_D' :0.3 ,'fichas_E' :0 ,'fichas_F' :0,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :True}
        elif novo_ficheiro == 2:
            ficheiro = {'pote' :0.75 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :'C2'
                        ,'bord_RIVER' :'C2',
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'aposta_A' :0 ,'aposta_B' :0.05 ,'aposta_C' :0.1 ,'aposta_D' :0.3 ,'aposta_E' :0.3
                        ,'aposta_F' :0,
                        'fichas_A' :0 ,'fichas_B' :0.05 ,'fichas_C' :0.1 ,'fichas_D' :0.3 ,'fichas_E' :0 ,'fichas_F' :0,
                        'vez_A' :True ,'vez_B' :False ,'vez_C' :False ,'vez_D' :False ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :False ,'hole_cards_B' :False ,'hole_cards_C' :False ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :True}
        elif novo_ficheiro == 3:
            ficheiro = {'pote' :4.04 ,'pote_rodada' :0.00 ,'bord_etapa' :'RIVER' ,'mao' :1,
                        'bord_FLOP_1' :'C2' ,'bord_FLOP_2' :'C2' ,'bord_FLOP_3' :'C2' ,'bord_TURN' :'C2'
                        ,'bord_RIVER' :'C2',
                        'diler_A' :True ,'diler_B' :False ,'diler_C' :False ,'diler_D' :False ,'diler_E' :False
                        ,'diler_F' :False,
                        'aposta_A' :0 ,'aposta_B' :0.1 ,'aposta_C' :0.3 ,'aposta_D' :0.3 ,'aposta_E' :0.3
                        ,'aposta_F' :0,
                        'fichas_A' :0 ,'fichas_B' :0.05 ,'fichas_C' :0.1 ,'fichas_D' :0.3 ,'fichas_E' :0 ,'fichas_F' :0,
                        'vez_A' :False ,'vez_B' :False ,'vez_C' :False ,'vez_D' :True ,'vez_E' :False ,'vez_F' :False,
                        'hole_cards_A' :True ,'hole_cards_B' :False ,'hole_cards_C' :True ,'hole_cards_D' :False
                        ,'hole_cards_E' :False ,'hole_cards_F' :True}
        return ficheiro


if __name__ == "__main__":
    print('Teste da classe lisnhas descartavel')
    unittest.main()
