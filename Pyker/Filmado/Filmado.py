import threading
from .. import Fotografo
from .. import cenografo
from .. import Registrado
from .. import Dados


class Filmado(threading.Thread):

    def __init__(self, lista_de_cartas, tela, url, numero_de_cartas=30):
        self.lista_de_cartas = lista_de_cartas
        self.tela = tela
        self.numero_de_cartas = numero_de_cartas
        self.registrador = Registrado.Registrado(self.lista_de_cartas)
        self.fotografo = Fotografo.Fotografo(self.lista_de_cartas)
        self.cenografo = cenografo.Cenografo('MPSC6', self.lista_de_cartas)
        self.dados = Dados.Dados(self.lista_de_cartas,url)
        self.registrador.listar_telas()
        self.registrador.organizar_telas()
        threading.Thread.__init__(self)

    def run(self):
        self.registrar()

    def registrar(self):
        while self.quantidade_cartas_novas() <= self.numero_de_cartas:
            index = self.registrador.registrar(self.tela)
            self.fotografo.fotografar(index)
            self.cenografo.cenofrafar(index)
            print(self.tela, self.quantidade_cartas_novas(), len(self.lista_de_cartas))
            self.dados.registrar_imagem(index)
            self.dados.salvar_cenografo(index)
        print('fim da tread: ', self.tela)

    def quantidade_cartas_novas(self):
        contador = 0
        for item in self.lista_de_cartas:
            if item['nova_carta'] == True:
                contador += 1
        return contador


