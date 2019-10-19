import random

class Funcoes_Axiliares(object):

    def __init__(self):
        pass


    def retornar_lista_telas_embaralhadas(self,tamanho,telas):
        quadros_por_tela = {}
        telas_embaralhadas = []

        for telas in range(1,telas+1):
            quadros_por_tela.setdefault(telas,0)

        while True:
            if len(telas_embaralhadas) >= (tamanho*telas):
                break
            else:
                valor = random.randint(1,telas)
                if quadros_por_tela[valor] < tamanho:
                    telas_embaralhadas.append((valor,quadros_por_tela[valor]))
                    quadros_por_tela[valor] += 1

        return telas_embaralhadas