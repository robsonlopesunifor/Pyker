import unittest
import cv2
from pprint import pprint
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
import Pyker.cenografo as Cenografo


class CenografoTest(unittest.TestCase):

    def test_cenas(self):
        print('-------------test_fotografa---------------')
        lista_de_cartas = []
        cenografo = Cenografo.Cenografo('MPSC6',lista_de_cartas)
        imagem_1 = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_4.jpg')
        imagem_2 = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_5.jpg')

        lista_de_cartas.append({'imagem': imagem_1, 'cenografo': None, 'nova_carta': False, 'tela':1})
        lista_de_cartas.append({'imagem': imagem_2, 'cenografo': None, 'nova_carta': False, 'tela': 2})
        lista_de_cartas.append({'imagem': imagem_1, 'cenografo': None, 'nova_carta': False, 'tela':1})
        lista_de_cartas.append({'imagem': imagem_2, 'cenografo': None, 'nova_carta': False, 'tela': 2})
        lista_de_cartas.append({'imagem': imagem_2, 'cenografo': None, 'nova_carta': False, 'tela':1})
        lista_de_cartas.append({'imagem': imagem_1, 'cenografo': None, 'nova_carta': False, 'tela': 2})
        lista_de_cartas.append({'imagem': imagem_2, 'cenografo': None, 'nova_carta': False, 'tela':1})
        lista_de_cartas.append({'imagem': imagem_1, 'cenografo': None, 'nova_carta': False, 'tela': 2})

        cenografo.cenofrafar(0)
        self.assertEqual(lista_de_cartas[0]['nova_carta'],True)
        cenografo.cenofrafar(1)
        self.assertEqual(lista_de_cartas[1]['nova_carta'], True)
        cenografo.cenofrafar(2)
        self.assertEqual(lista_de_cartas[2]['nova_carta'],False)
        cenografo.cenofrafar(3)
        self.assertEqual(lista_de_cartas[3]['nova_carta'], False)
        cenografo.cenofrafar(4)
        self.assertEqual(lista_de_cartas[4]['nova_carta'],True)
        cenografo.cenofrafar(5)
        self.assertEqual(lista_de_cartas[5]['nova_carta'], True)
        cenografo.cenofrafar(6)
        self.assertEqual(lista_de_cartas[6]['nova_carta'],False)
        cenografo.cenofrafar(7)
        self.assertEqual(lista_de_cartas[7]['nova_carta'], False)

if __name__ == "__main__":
    print('____Teste da classe Cenografo')
    unittest.main()
