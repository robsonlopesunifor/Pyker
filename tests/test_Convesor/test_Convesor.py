import unittest
from pprint import pprint
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
print(sys.path[0])
import Pyker.Convesor as Convesor

class ConvesorTest(unittest.TestCase):

    def test_carregar(self):
        print('---------- test_carregar -------------')
        convesor = Convesor.Convesor()
        arquivo = "HH20190525 Halley - US$ 0,01-US$ 0,02 - USD No Limit Hold'em.txt"
        convesor.arquivo = arquivo
        convesor.converter_hand_history_em_excel()


if __name__ == "__main__":
    print('____Teste da classe Convesor')
    unittest.main()