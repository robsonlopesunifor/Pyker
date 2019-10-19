import unittest
from datetime import datetime
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
print(sys.path[0])
import Pyker.Dados as Dados

class DadosTest(unittest.TestCase):

    def test_salvar_cenografo(self):
        print('===============================[ test_salvar ]===============================')
        lista_de_cartas = []
        lista_de_cartas.append(self.gerar_cenografo())
        dados = Dados.Dados(lista_de_cartas,'http://localhost:8000/cenografo/')
        dados.salvar_cenografo(0)

    def gerar_cenografo(self):
        cena = {
                "titulo": "Amundsen - US$ 0,08/US$ 0,16 USD - No Limit Hold'em",
                "tela": 1,
                "data": '2019-07-19 17:02:42',
                "chave": '20190719170242-1-00',
                "foto": '',
                "fotografo_processado": True,
                "endereco_imegem": 'http://localhost',
                "foto_salva": False,
                "cenografo_processado": False,
                "cena_salva": False,
                "cientista_processado": False,
                "cientista_salva": False,
                "nova_carta": False,
                "recorte": (-10, 364, 504, 374),
                "mesa": 0,
                "cena": {
                    "data": {
                        "A":"2019-07-19T23:00:00Z"
                    },
                    "pote": {
                        "A": 0.0
                    },
                    "pote_rodada": {
                        "A": 0.0
                    },
                    "bord": {
                        "FLOP_1": "",
                        "FLOP_2": "",
                        "FLOP_3": "",
                        "TURN": "",
                        "RIVER": ""
                    },
                    "combo": {
                        "A_1": "",
                        "A_2": "",
                        "B_1": "",
                        "B_2": "",
                        "C_1": "",
                        "C_2": "",
                        "D_1": "",
                        "D_2": "",
                        "E_1": "",
                        "E_2": "",
                        "F_1": "",
                        "F_2": ""
                    },
                    "fichas": {
                        "A": 0.0,
                        "B": 0.0,
                        "C": 0.0,
                        "D": 0.0,
                        "E": 0.0,
                        "F": 0.0
                    },
                    "aposta": {
                        "A": 0.0,
                        "B": 0.0,
                        "C": 0.0,
                        "D": 0.0,
                        "E": 0.0,
                        "F": 0.0
                    },
                    "hole_cards": {
                        "A": True,
                        "B": False,
                        "C": False,
                        "D": False,
                        "E": False,
                        "F": False
                    },
                    "vez": {
                        "A": True,
                        "B": False,
                        "C": False,
                        "D": False,
                        "E": False,
                        "F": False
                    },
                    "diler": {
                        "A": True,
                        "B": False,
                        "C": False,
                        "D": False,
                        "E": False,
                        "F": False
                    },
                    "tela": {
                        "A": 0
                    }
                }
            }

        return cena




if __name__ == "__main__":
    print('____Teste da classe Dados')
    unittest.main()