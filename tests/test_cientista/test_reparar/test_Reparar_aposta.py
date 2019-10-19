import unittest
import pandas as pd
import sys, os
sys.path.insert(-1,os.path.abspath('../../../Pyker'))
import cientista.Reparar.Reparar_aposta as Reparar
from Cenografo.tests.test_cientista.Auxiliar import Auxiliar


class Reparar_aposta_test(unittest.TestCase,Auxiliar):

    def test_validar(self):
        print('------------ validar -----------------')
        df_embaralhado = self.embaralhar_dataframe('datagrama.csv',3)
        df = pd.DataFrame(columns=df_embaralhado.columns)
        reparar_aposta = Reparar.Reparar_aposta()
        reparar_aposta.iniciar(df, ['A', 'B', 'C', 'D', 'E', 'F'])
        for x in range(len(df_embaralhado)):
            df.loc[x] = df_embaralhado.iloc[x].copy()
            reparar_aposta.reparar(x)
        self.mostrar_resultado(df)

        tela_1 = df[df['tela'] == 1].drop(['tela'], axis=1).to_string(index=False)
        tela_2 = df[df['tela'] == 2].drop(['tela'], axis=1).to_string(index=False)
        tela_3 = df[df['tela'] == 3].drop(['tela'], axis=1).to_string(index=False)

        self.assertEqual(tela_1, tela_2)
        self.assertEqual(tela_1, tela_3)
        self.assertEqual(tela_2, tela_3)

    def mostrar_resultado(self ,df):
        lista_index = df[(df['valido_aposta_A'] == False) |
                         (df['valido_aposta_B'] == False) |
                         (df['valido_aposta_C'] == False) |
                         (df['valido_aposta_D'] == False) |
                         (df['valido_aposta_E'] == False) |
                         (df['valido_aposta_F'] == False) ].index.values

        for linha in lista_index:
            linha_anterior = linha - 1
            print('------------------------------------------------------- ')
            print(df.loc[linha_anterior:linha_anterior,('fichas_A' ,'fichas_B' ,'fichas_C' ,'fichas_D' ,'fichas_E' ,'fichas_F')])
            print(df.loc[linha_anterior:linha_anterior,('aposta_A' ,'aposta_B' ,'aposta_C' ,'aposta_D' ,'aposta_E' ,'aposta_F')])

            print(df.loc[linha:linha ,('fichas_A' ,'fichas_B' ,'fichas_C' ,'fichas_D' ,'fichas_E' ,'fichas_F')])
            print(df.loc[linha:linha ,('aposta_A' ,'aposta_B' ,'aposta_C' ,'aposta_D' ,'aposta_E' ,'aposta_F')])




    def gerador_de_ficheiros(self ,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :5.00 ,'fichas_B' :5.00 ,'fichas_C' :5.00 ,'fichas_D' :5.00 ,'fichas_E' :0
                        ,'fichas_F' :5.00,
                        'valido_aposta_A' :True ,'valido_aposta_B' :True ,'valido_aposta_C' :True
                        ,'valido_aposta_D' :True ,'valido_aposta_E' :True ,'valido_aposta_F' :True}
        elif novo_ficheiro == 1:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :5.00 ,'fichas_B' :5.00 ,'fichas_C' :5 ,'fichas_D' :5.00 ,'fichas_E' :5.00
                        ,'fichas_F' :5.00,
                        'valido_aposta_A' :True ,'valido_aposta_B' :True ,'valido_aposta_C' :True
                        ,'valido_aposta_D' :True ,'valido_aposta_E' :True ,'valido_aposta_F' :True}
        elif novo_ficheiro == 2:
            ficheiro = {'mao' :11,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :4 ,'fichas_B' :4 ,'fichas_C' :4 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'valido_aposta_A' :True ,'valido_aposta_B' :True ,'valido_aposta_C' :True
                        ,'valido_aposta_D' :True ,'valido_aposta_E' :True ,'valido_aposta_F' :True}
        elif novo_ficheiro == 3:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :2 ,'aposta_C' :2 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :3 ,'fichas_B' :3 ,'fichas_C' :3 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'valido_aposta_A' :False ,'valido_aposta_B' :True ,'valido_aposta_C' :True
                        ,'valido_aposta_D' :True ,'valido_aposta_E' :True ,'valido_aposta_F' :True}
        elif novo_ficheiro == 4:
            ficheiro = {'mao' :11,
                        'aposta_A' :0 ,'aposta_B' :0 ,'aposta_C' :0 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :3 ,'fichas_B' :3 ,'fichas_C' :3 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'valido_aposta_A' :True ,'valido_aposta_B' :True ,'valido_aposta_C' :True
                        ,'valido_aposta_D' :True ,'valido_aposta_E' :True ,'valido_aposta_F' :True}
        elif novo_ficheiro == 5:
            ficheiro = {'mao' :11,
                        'aposta_A' :1 ,'aposta_B' :1 ,'aposta_C' :1 ,'aposta_D' :0 ,'aposta_E' :0 ,'aposta_F' :0,
                        'fichas_A' :2 ,'fichas_B' :2 ,'fichas_C' :2 ,'fichas_D' :0 ,'fichas_E' :0 ,'fichas_F' :0,
                        'valido_aposta_A' :True ,'valido_aposta_B' :True ,'valido_aposta_C' :True
                        ,'valido_aposta_D' :True ,'valido_aposta_E' :True ,'valido_aposta_F' :True}

        return ficheiro



if __name__ == "__main__":
    print('Teste da classe Regra aposta')
    unittest.main()
