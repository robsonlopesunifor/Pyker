import unittest
from datetime import datetime
from pprint import pprint
import sys, os
sys.path.insert(0, os.path.abspath('../../Pyker'))
import Registrado as Registrado
import Fotografo as Fotografo

class FotografoTest(unittest.TestCase):

    def test_fotografar(self):
        print('===============================[ test_iniciar ]===============================')
        lista_de_cartas = []
        registrado = Registrado.Registrado(lista_de_cartas)
        fotografo = Fotografo.Fotografo(lista_de_cartas)
        registrado.listar_telas()
        registrado.organizar_telas()
        index = registrado.registrar(0)
        fotografo.fotografar(index)
        index = registrado.registrar(1)
        print(lista_de_cartas)
        fotografo.fotografar(index)

    def test_show(self):
        print('===============================[ test_iniciar ]===============================')
        lista_de_cartas = []
        registrado = Registrado.Registrado(lista_de_cartas)
        fotografo = Fotografo.Fotografo(lista_de_cartas)
        registrado.listar_telas()
        registrado.organizar_telas()
        index = registrado.registrar(0)
        fotografo.fotografar(index)
        index = registrado.registrar(1)
        fotografo.fotografar(index)
        fotografo.show()

    """ 
    def salvar_imagem(self):
        print('===============================[ salvar_imagem ]===============================')
        fotografo = Fotografo.Fotografo()
        fotografo.registrar_lista_de_mesas()
        for chave in fotografo.dicionario_de_mesas:
            print(chave)
            if input('1 / 0 : ') == 1:
                fotografo.iniciar(2)
                fotografo.fotografar_mesa(chave)
                fotografo.salvar_imagem('')
    """

if __name__ == "__main__":
    print('____Teste da classe Fotografo')
    unittest.main()