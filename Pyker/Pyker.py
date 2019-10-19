from . import Fotografo
from . import cenografo
from . import cientista

class Pyker:

    def __init__(self):
        self.lista_de_cartas = []
        self.fotografo = Fotografo.Fotografo(self.lista_de_cartas)
        self.cenografo = cenografo.Cenografo('MPSC6',self.lista_de_cartas)
        self.cientista = cientista.Cientista(self.lista_de_cartas)

    def registrar(self,numerp_de_cartas):
        while len(self.lista_de_cartas) <= numerp_de_cartas:
            print(len(self.lista_de_cartas))
            self.fotografo.fotografar()
            self.cenografo.cenofrafar()
            self.cientista.processar()

