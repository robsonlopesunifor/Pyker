import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
print(sys.path[0])
import Pyker.Visor as Visor

class VisorTest(unittest.TestCase):

    def test_show(self):
        print('===============================[ test_salvar ]===============================')
        visor = Visor.Visor()
        visor.show()



if __name__ == "__main__":
    print('____Teste da classe Visor')
    unittest.main()