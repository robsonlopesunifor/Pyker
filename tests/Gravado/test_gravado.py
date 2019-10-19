import unittest
import sys, os
import pandas as pd
sys.path.insert(0, os.path.abspath('../../'))
print(sys.path[0])
import Pyker.Gravado as Gravado
import time
import Pyker.Registrado as Registrado

class GravadoTest(unittest.TestCase):

    def _test_Gravado(self):
        print('===============================[ test_Filmado ]===============================')
        pandas = pd.DataFrame()
        lista_de_carta = self.gerar_lista_de_cartas()

        gravado = Gravado.Gravado(lista_de_carta, pandas, 'localhost', 27017)
        gravado.start()

        time.sleep(10)
        gravado.gravando = False
        gravado.join()

        print('Saindo da Thread principal.')

    def test_Gravado_do_mongoDB(self):
        print('===============================[ test_Filmado ]===============================')
        pandas = pd.DataFrame()
        lista_de_carta = []

        gravado = Gravado.Gravado(lista_de_carta, pandas, 'localhost', 27017)
        gravado.start()

        gravado.join()

        print('Saindo da Thread principal.')

    def gerar_lista_de_cartas(self):
        # lista com duas telas
        # tela 0 : 5 cartas, 4 cenografos 1 cientistas
        # tela 1 : r cartas, 5 cenografos 5 cinetistas

        lista_de_telas = [{'tela': 0,'nova_carta': True, 'cenografo': self.retorna_fichario(0), 'cientista': {'':''}},
                          {'tela': 1,'nova_carta': True, 'cenografo': self.retorna_fichario(1), 'cientista': {'':''}},
                          {'tela': 0,'nova_carta': True, 'cenografo': self.retorna_fichario(0), 'cientista': {'':''}},
                          {'tela': 1,'nova_carta': True, 'cenografo': self.retorna_fichario(1), 'cientista': {'':''}},
                          {'tela': 0,'nova_carta': True, 'cenografo': self.retorna_fichario(0), 'cientista': None},
                          {'tela': 1,'nova_carta': True, 'cenografo': self.retorna_fichario(1), 'cientista': {'':''}},
                          {'tela': 0,'nova_carta': True, 'cenografo': self.retorna_fichario(0), 'cientista': None},
                          {'tela': 1,'nova_carta': True, 'cenografo': self.retorna_fichario(1), 'cientista': None},
                          {'tela': 0,'nova_carta': True, 'cenografo': self.retorna_fichario(0), 'cientista': None},
                          {'tela': 1,'nova_carta': True, 'cenografo': self.retorna_fichario(1), 'cientista': None}]

        return lista_de_telas

    def retorna_fichario(self,tela):
        fichario = {'fichas':{'A':1.00, 'B':0.00, 'C':0.00, 'D':0.00, 'E':0.00, 'F':0.00},
                    'vez':{'A':True, 'B':True, 'C':True, 'D':False, 'E':True, 'F':True},
                    'diler':{'A':True, 'B':True, 'C':True, 'D':False, 'E':True, 'F':True},
                    'pote':{'A':0.15},
                    'pote_rodada':{'A':0.00},
                    'aposta':{'A':0.05, 'B':0.10, 'C':0.00, 'D':0.00, 'E':0.00, 'F':0.00},
                    'bord':{'FLOP_1':'O3', 'FLOP_2':'O3', 'FLOP_3':'O3', 'TURN':'O3', 'RIVER':'O3'},
                    'hole_cards':{'A':False, 'B':False, 'C':True, 'D':False, 'E':True, 'F':True},
                    'combo':{'A_1':'', 'B_1':'', 'C_1':'', 'D_1':'', 'E_1':'', 'F_1':'',
                             'A_2':'', 'B_2':'', 'C_2':'', 'D_2':'', 'E_2':'', 'F_2':''},
                    'tela':{'A':tela},
                    'data':{'A':'2019-11-09'},}

        return fichario

if __name__ == "__main__":
    print('____Teste da classe Pyker')
    unittest.main()
