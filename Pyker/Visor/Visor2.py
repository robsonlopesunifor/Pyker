import cv2
import pandas as pd
import numpy as np
import sys, os
from copy import copy, deepcopy
from .. import Registrado
from .. import Fotografo
from .. import cenografo


class Visor:

    def __init__(self):
        self.tela = 0
        self.lista_de_cartas = []
        self.pausar = False
        self.registrador = Registrado.Registrado(self.lista_de_cartas)
        self.fotografo = Fotografo.Fotografo(self.lista_de_cartas)
        self.cenografo = cenografo.Cenografo('MPSC6', self.lista_de_cartas)
        self.registrador.listar_telas()
        self.registrador.organizar_telas()

    def show(self):
        
        self.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        cv2.namedWindow('Ajuste')
        while(1):
            if self.pausar != True:
                index = self.registrador.registrar(self.tela)
                self.fotografo.fotografar(index)
                self.cenografo.cenofrafar(index)
            img = copy(self.ultimaImagemPorTela(self.tela)) 
            self.cenografo.ficheiro.set_imagem(img)
            #self.cenografo.ficheiro.marcar()
            #self.gravar_jogadas()
            #self.marcar()
            cv2.imshow('Ajuste',img)
            key = cv2.waitKey(33)
            #self.menu(key)
            if key == 27:
                break
        cv2.destroyAllWindows()

    def ultimaImagemPorTela(self,tela):
        for carta in reversed(self.lista_de_cartas):
            if carta['fotografo_processado'] == True and carta['tela'] == tela:
                #print(carta['cena'])
                return carta['foto']
