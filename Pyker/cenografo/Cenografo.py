from . import Ficheiro as Ficheiro
from copy import deepcopy

class Cenografo(object):

    def __init__(self,modelo,lista_de_cartas=[]):
        self.lista_de_cartas = lista_de_cartas
        self.ficheiro = Ficheiro.Ficheiro({'modelo':modelo})
        self.ficheiro.ler_molde('dados.json')


    def cenofrafar(self,index):
        cartas = self.lista_de_cartas[index]
        self.ficheiro.set_imagem(cartas['foto'])
        ficheiro = deepcopy(self.ficheiro.comparar())
        ficheiro.setdefault('tela',{'A':cartas['tela']})
        ficheiro.setdefault('data', {'A': cartas['data']})
        cartas['cena'] = ficheiro
        cartas['cenografo_processado'] = True
        cartas['nova_carta'] = self.nova_carta(index)


    def nova_carta(self,index):
        if index > 0:
            for decremento in range(1,index+1):
                idx_reverco = index - decremento
                anterior = self.lista_de_cartas[idx_reverco]
                atual = self.lista_de_cartas[index]
                if (atual['tela'] == anterior['tela']):
                    ficheiro_atual = deepcopy(atual['cena'])
                    ficheiro_anterior = deepcopy(anterior['cena'])
                    for chave, valor in ficheiro_atual.items():
                        if (chave != 'data' and chave != 'data_dia' and chave != 'data_hora' ) and ficheiro_atual[chave] != ficheiro_anterior[chave]:
                            return True # se for diferente do anterior, ira chegar aqui.
                    return False # se for igual ao anterior, ira chegar aqui.
        else:
            return True # se for o primeiro retorne True

