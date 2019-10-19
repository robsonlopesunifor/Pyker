import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../../Pyker'))
import Registrado as Registrado

class FotografoTest(unittest.TestCase):

    def test_lista_de_telas(self):
        print('===============================[ test_lista_de_telas ]===============================')
        lista_de_telas = [{'titulo':"No Limit Hold'em 1",'ativo':True,'recorte':()},
                          {'titulo':'tela 2','ativo':True,'recorte':()}]
        registrado = Registrado.Registrado()
        registrado.lista_de_telas = lista_de_telas
        registrado.listar_telas()
        self.assertEqual(len(registrado.lista_de_telas),5)
        self.assertEqual(registrado.lista_de_telas[0]['ativo'], False)
        self.assertEqual(registrado.lista_de_telas[1]['ativo'], False)
        registrado.listar_telas()
        self.assertEqual(len(registrado.lista_de_telas),5)

    def test_organizar_telas(self):
        print('===============================[ test_organizar_telas ]===============================')
        registrado = Registrado.Registrado()
        registrado.listar_telas()
        registrado.organizar_telas()

    def test_registrar(self):
        print('===============================[ test_registrar ]===============================')
        registrado = Registrado.Registrado()
        registrado.listar_telas()
        registrado.registrar(0)
        self.assertEqual(len(registrado.lista_de_cartas), 1)
        registrado.registrar(1)
        self.assertEqual(len(registrado.lista_de_cartas), 2)
        registrado.registrar(2)
        self.assertEqual(len(registrado.lista_de_cartas), 3)

    def test_quantidade_de_cartas_pendentes_por_categoria(self):
        print('===============================[ test_quantidade_de_cartas_pendentes_por_categoria ]===============================')
        registrador = Registrado.Registrado(self.gerar_lista_de_cartas())

        cenografo_pendente = registrador.quantidade_de_cartas_registradas(0, 'cenografo')
        self.assertEqual(cenografo_pendente, 4)
        cientista_pendente = registrador.quantidade_de_cartas_registradas(0, 'cientista')
        self.assertEqual(cientista_pendente, 3)
        cenografo_pendente = registrador.quantidade_de_cartas_registradas(1, 'cenografo')
        self.assertEqual(cenografo_pendente, 5)
        cientista_pendente = registrador.quantidade_de_cartas_registradas(1, 'cientista')
        self.assertEqual(cientista_pendente, 4)

    def _test_index_da_carta_penedente_por_categoria(self):
        print('===============================[ test_index_da_carta_penedente_por_categoria ]===============================')
        registrador = Registrado.Registrado(self.gerar_lista_de_cartas())

        index_cenografo_pendente = registrador.index_da_carta_penedente_por_categoria(0, 'cenografo')
        self.assertEqual(index_cenografo_pendente, 5)
        index_cientista_pendente = registrador.index_da_carta_penedente_por_categoria(0, 'cientista')
        self.assertEqual(index_cientista_pendente, 4)
        index_cenografo_pendente = registrador.index_da_carta_penedente_por_categoria(1, 'cenografo')
        self.assertEqual(index_cenografo_pendente, 6)
        index_cientista_pendente = registrador.index_da_carta_penedente_por_categoria(1, 'cientista')
        self.assertEqual(index_cientista_pendente, 5)

    def gerar_lista_de_cartas(self):
        # lista com duas telas
        # tela 0 : 5 cartas 4 cenografos 3 cientistas
        # tela 1 : r cartas 5 cenografos 4 cinetistas

        lista_de_telas = [{'tela': 0, 'cenografo': {'':''}, 'cientista': {'':''}},
                          {'tela': 1, 'cenografo': {'':''}, 'cientista': {'':''}},
                          {'tela': 0, 'cenografo': {'':''}, 'cientista': {'':''}},
                          {'tela': 1, 'cenografo': {'':''}, 'cientista': {'':''}},
                          {'tela': 0, 'cenografo': {'':''}, 'cientista': {'':''}},
                          {'tela': 1, 'cenografo': {'':''}, 'cientista': {'':''}},
                          {'tela': 0, 'cenografo': {'':''}, 'cientista': None},
                          {'tela': 1, 'cenografo': {'':''}, 'cientista': {'':''}},
                          {'tela': 0, 'cenografo': None,    'cientista': None},
                          {'tela': 1, 'cenografo': {'':''}, 'cientista': None}]

        return lista_de_telas




if __name__ == "__main__":
    print('____Teste da classe Registrado')
    unittest.main()