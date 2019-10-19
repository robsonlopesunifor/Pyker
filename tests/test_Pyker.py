import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../'))
print(sys.path[0])
import Pyker.Pyker as Pyker

class PykerTest(unittest.TestCase):

    def test_registrar(self):
        print('===============================[ test_registrar ]===============================')
        pyker = Pyker.Pyker()
        pyker.registrar(30)
        print(len(pyker.lista_de_cartas))

        for idx,cartas in enumerate(pyker.lista_de_cartas):
            print(cartas['nova_carta'])

        dataframe = pyker.cientista.dataframe

        print(dataframe[dataframe['tela'] == 1].loc[:,('bord_FLOP_1','bord_FLOP_2','bord_FLOP_3','bord_TURN','bord_RIVER')])
        print(dataframe[dataframe['tela'] == 2].loc[:,('bord_FLOP_1','bord_FLOP_2','bord_FLOP_3','bord_TURN','bord_RIVER')])
        print(dataframe[dataframe['tela'] == 3].loc[:,('bord_FLOP_1','bord_FLOP_2','bord_FLOP_3','bord_TURN','bord_RIVER')])


if __name__ == "__main__":
    print('____Teste da classe Pyker')
    unittest.main()