import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_pote_rodada as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Reparar_pote_rodada_test(unittest.TestCase,Auxiliar):

    def test_repara(self):
        print('------------ validar -----------------')
        reparar_pote_rodada = Reparar.Reparar_pote_rodada()
        dataframe = pd.DataFrame()
        reparar_pote_rodada.iniciar(dataframe ,['A' ,'B' ,'C' ,'D' ,'E' ,'F'])
        self.reparar_dicionario_com_telas_embaralhadas(dataframe,reparar_pote_rodada,6,3)
        print(reparar_pote_rodada.dataframe)

        tela_1 = dataframe[dataframe['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = dataframe[dataframe['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = dataframe[dataframe['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)


    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote' :2.23 ,'pote_rodada' :1.00 ,'valido_pote_rodada' :True ,'mao' :1 ,'bord_etapa' :1,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :1 ,'aposta_E' :1 ,'aposta_F' :1}
        elif novo_ficheiro == 1:
            ficheiro = {'pote' :2.23 ,'pote_rodada' :2.23 ,'valido_pote_rodada' :True ,'mao' :1 ,'bord_etapa' :2,
                        'aposta_A' :1.20 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :1 ,'aposta_E' :1 ,'aposta_F' :1}
        elif novo_ficheiro == 2:
            ficheiro = {'pote' :5.83 ,'pote_rodada' :5.00 ,'valido_pote_rodada' :False ,'mao' :1 ,'bord_etapa' :2,
                        'aposta_A' :1.20 ,'aposta_B' :1.20 ,'aposta_C' :1.20 ,'aposta_D' :1 ,'aposta_E' :1
                        ,'aposta_F' :1}
        elif novo_ficheiro == 3:
            ficheiro = {'pote' :5.83 ,'pote_rodada' :0.0 ,'valido_pote_rodada' :False ,'mao' :1 ,'bord_etapa' :3,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :1 ,'aposta_E' :1 ,'aposta_F' :1}
        elif novo_ficheiro == 4:
            ficheiro = {'pote' :5.83 ,'pote_rodada' :0.0 ,'valido_pote_rodada' :False ,'mao' :1 ,'bord_etapa' :3,
                        'aposta_A' :1.20 ,'aposta_B' :1.20 ,'aposta_C' :1.20 ,'aposta_D' :1 ,'aposta_E' :1
                        ,'aposta_F' :1}
        elif novo_ficheiro == 5:
            ficheiro = {'pote' :6.83 ,'pote_rodada' :0.0 ,'valido_pote_rodada' :False ,'mao' :1 ,'bord_etapa' :4,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :1 ,'aposta_E' :1 ,'aposta_F' :1}
        return ficheiro



if __name__ == "__main__":
    print('Teste da classe Regra pote rodada')
    unittest.main()
