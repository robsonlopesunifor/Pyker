import unittest
from pprint import pprint
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
print(sys.path[0])
import Pyker.HandHistory as HandHistory

class HandHistoryTest(unittest.TestCase):

    def test_carregar(self):
        print('---------- test_carregar -------------')
        arquivo = "HH20190525 Halley - US$ 0,01-US$ 0,02 - USD No Limit Hold'em.txt"
        hand = HandHistory.HandHistory()
        hand.arquivo = arquivo
        hand.percorrer_historico_de_mao()

    def test_lista_de_ficheiros(self):
        print('---------- test_lista_de_ficheiros -------------')
        arquivo = "HH20190525 Halley - US$ 0,01-US$ 0,02 - USD No Limit Hold'em.txt"
        hand = HandHistory.HandHistory()
        hand.arquivo = arquivo
        lista_de_ficheiros = hand.gerar_lista_de_ficheiros()
        #pprint(lista_de_ficheiros)


if __name__ == "__main__":
    print('____Teste da classe Dados')
    unittest.main()