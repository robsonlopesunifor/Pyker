import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_vencedor as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Reparar_vencedor_test(unittest.TestCase,Auxiliar):

    def test_validar(self):
        print('------------ validar -----------------')
        df_embaralhado = self.embaralhar_dataframe('datagrama.csv', 3)
        df = pd.DataFrame(columns=df_embaralhado.columns)
        reparar_vencedor = Reparar.Reparar_vencedor()
        reparar_vencedor.iniciar(df, ['A', 'B', 'C', 'D', 'E', 'F'])
        for x in range(len(df_embaralhado)):
            df.loc[x] = df_embaralhado.iloc[x].copy()
            reparar_vencedor.reparar(x)
        print(reparar_vencedor.dataframe.loc[:, ('vencedor')])

        tela_1 = df[df['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = df[df['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = df[df['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)



    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'linha':'normal','aposta_A':0,'aposta_B':0,'aposta_C':0,'aposta_D':0,'aposta_E':0,'aposta_F':0}
        elif novo_ficheiro == 1:
            ficheiro = {'linha':'descartavel','aposta_A':0,'aposta_B':0,'aposta_C':0,'aposta_D':0,'aposta_E':0,'aposta_F':0}
        elif novo_ficheiro == 2:
            ficheiro = {'linha':'descartavel','aposta_A':0,'aposta_B':0,'aposta_C':0,'aposta_D':0,'aposta_E':0,'aposta_F':0}
        elif novo_ficheiro == 3:
            ficheiro = {'linha':'normal','aposta_A':0,'aposta_B':0,'aposta_C':-2.0,'aposta_D':0,'aposta_E':0,'aposta_F':0}
        return ficheiro


if __name__ == "__main__":
    print('Teste da classe vencedor')
    unittest.main()
