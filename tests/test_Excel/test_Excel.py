import unittest
import pandas as pd
from datetime import datetime
import sys, os
from pprint import pprint
sys.path.insert(0, os.path.abspath('../../'))
print(sys.path[0])
import Pyker.Excel as Excel
import Pyker.Dados as Dados


class TabelaTest(unittest.TestCase):

    def _test_iniciar(self):
        print('---------- iniciar -------------')
        painel_excel = Excel.Salvar_execel()
        df = self.gerador_dataframe()
        painel_excel.iniciar(df)

    def _test_salvar(self):
        print('---------- iniciar -------------')
        salvar_execel = Excel.Excel()
        # df = self.gerador_dataframe()
        file_name_csv = 'mesas.csv'
        df = pd.read_csv(file_name_csv, sep=';')
        file_name = 'example.xlsx'
        salvar_execel.iniciar(df)
        # salvar_execel.iniciar(df[df['linha'] != 'descartavel'])
        # salvar_execel.iniciar(df[(df['linha'] != 'descartavel') & (df['nome_acao'] != 'FOLD')])
        salvar_execel.salvar(file_name)

    def test_carregar_pandas(self):
        print('---------- carregar pandas -------------')
        lista_de_cartas = []
        dados = Dados.Dados('localhost', 27017, lista_de_cartas)
        dados.get_colecao('Pyker', 'cientista')
        inicio = datetime(2019, 4, 29)
        fim = datetime(2019, 7, 16)
        pandas = dados.carregar_pandas({'tela':0.0,'data':{'$gt': fim}})

        salvar_execel = Excel.Excel()
        file_name = 'example2.xlsx'
        salvar_execel.iniciar(pandas)
        # salvar_execel.iniciar(df[df['linha'] != 'descartavel'])
        # salvar_execel.iniciar(df[(df['linha'] != 'descartavel') & (df['nome_acao'] != 'FOLD')])
        salvar_execel.salvar(file_name)


    def gerador_dataframe(self):
        data = {'mao': [11, 11, 11, 11, 12, 12, 12, 12],

                'diler_A': [False, False, False, False, False, False, False, False],
                'diler_B': [True, True, True, True, False, False, False, False],
                'diler_C': [False, False, False, False, False, False, False, False],
                'diler_D': [False, False, False, False, False, False, False, False],
                'diler_E': [False, False, False, False, True, True, True, True],
                'diler_F': [False, False, False, False, False, False, False, False],

                'hole_cards_A': [True, True, False, False, True, True, True, False],
                'hole_cards_B': [True, False, True, True, True, True, True, True],
                'hole_cards_C': [True, True, True, False, True, True, False, True],
                'hole_cards_D': [True, True, True, True, True, False, True, True],
                'hole_cards_E': [True, True, False, True, True, True, True, True],
                'hole_cards_F': [True, True, True, True, True, True, True, False],

                'vez_A': [True, False, False, False, True, False, False, False],
                'vez_B': [False, True, False, False, False, True, False, False],
                'vez_C': [False, False, True, False, False, False, True, False],
                'vez_D': [False, False, False, True, False, False, False, True],
                'vez_E': [False, False, False, False, False, False, False, False],
                'vez_F': [False, False, False, False, False, False, False, False],

                'pote': [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],

                'pote_rodada': [0.00, 1.50, 2.50, 1.00, 2.00, 3.00, 3.50, 4.00],

                'aposta_A': [0.00, 0.50, 0.50, 0.00, 0.00, 0.00, 0.00, 0.00],
                'aposta_B': [0.00, 1.00, 1.00, 0.00, 1.00, 1.00, 1.00, 1.00],
                'aposta_C': [0.00, 0.00, 1.00, 0.00, 0.00, 1.00, 1.00, 1.00],
                'aposta_D': [0.00, 0.00, 0.00, 0.00, 1.00, 1.00, 1.50, 1.00],
                'aposta_E': [0.00, 0.00, 0.00, 1.00, 0.00, 0.00, 0.00, 1.00],
                'aposta_F': [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],

                'validado_aposta_A': [False, False, False, False, True, False, False, True],
                'validado_aposta_B': [False, False, False, False, True, False, False, False],
                'validado_aposta_C': [False, False, False, False, True, False, False, False],
                'validado_aposta_D': [False, True, False, False, True, False, True, False],
                'validado_aposta_E': [False, False, False, False, True, False, False, False],
                'validado_aposta_F': [True, False, False, False, True, False, False, False],

                'fichas_A': [5.00, 4.00, 3.00, 2.00, 5.00, 4.00, 3.00, 1.00],
                'fichas_B': [5.00, 4.00, 3.00, 2.00, 5.00, 4.00, 2.00, 1.00],
                'fichas_C': [5.00, 4.00, 4.00, 3.00, 5.00, 4.00, 2.00, 1.00],
                'fichas_D': [5.00, 5.00, 3.00, 2.00, 5.00, 4.00, 3.00, 2.00],
                'fichas_E': [5.00, 4.00, 3.00, 2.00, 5.00, 4.00, 2.00, 0.00],
                'fichas_F': [5.00, 5.00, 4.00, 3.00, 5.00, 4.00, 2.00, 1.00],

                'vilao_A': ['', '', '', '', '', '', '', ''],
                'vilao_B': ['', '', '', '', '', '', '', ''],
                'vilao_C': ['', '', '', '', '', '', '', ''],
                'vilao_D': ['', '', '', '', '', '', '', ''],
                'vilao_E': ['', '', '', '', '', '', '', ''],
                'vilao_F': ['', '', '', '', '', '', '', ''],

                'bord_FLOP_1': ['', '3C', '3C', '3C', '', '3C', '3C', '3C'],
                'bord_FLOP_2': ['', '5P', '5P', '5P', '', '5P', '5P', '5P'],
                'bord_FLOP_3': ['', '9P', '9P', '9P', '', '9P', '9P', '9P'],
                'bord_RIVER': ['', '', '9C', '9C', '', '', '9C', '9C'],
                'bord_TURN': ['', '', '', 'AE', '', '', '', 'AE']}

        df = pd.DataFrame(data)
        return df


if __name__ == "__main__":
    print('____Teste da classe Tabela')
    unittest.main()
