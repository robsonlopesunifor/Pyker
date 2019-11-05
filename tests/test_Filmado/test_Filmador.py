import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
print(sys.path[0])
import Pyker.Filmado as Filmado
import Pyker.Registrado as Registrado
import requests


class FilmadoTest(unittest.TestCase):

    def test_Filmado(self):
        print('===============================[ test_Filmado ]===============================')
        lista_de_carta = []
        terafas = []

        registrado = Registrado.Registrado(lista_de_carta)
        registrado.listar_telas()

        for idx in range(len(registrado.lista_de_telas)):
            tarefa = Filmado.Filmado(lista_de_carta, idx, 'http://localhost:8000/api/v1/cenografo/', 10)
            tarefa.start()
            terafas.append(tarefa)

        headers = {'content-type': 'application/json'}
        url = 'http://localhost:8002/api/v1/cientista_analizar'
        requests.post(url,headers=headers)

        #url = 'http://localhost:8002/api/v1/cenografo/salvar_imagens_do_redis/'
        #requests.post(url,headers=headers)

        for tarefa in terafas:
            tarefa.join()

        print('Saindo da Thread principal.')


if __name__ == "__main__":
    print('____Teste da classe Pyker')
    unittest.main()
