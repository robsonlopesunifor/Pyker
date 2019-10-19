import numpy
import cv2
import pyautogui
from matplotlib import pyplot as plt
from math import sqrt
from operator import add

class Fotografo:

    def __init__(self,lista_de_cartas=[]):
        self.lista_de_cartas = lista_de_cartas
        self.endereco_da_imegem_salma = ''

    def fotografar(self,index,ajuste=(10,0,-20,-10)):
        dupla = tuple(map(add, self.lista_de_cartas[index]['recorte'], ajuste))
        PILImage = pyautogui.screenshot(region=dupla)
        foto = cv2.cvtColor(numpy.array(PILImage), cv2.COLOR_RGB2BGR)
        self.lista_de_cartas[index]['foto'] = foto
        self.lista_de_cartas[index]['fotografo_processado'] = True


    def show(self):
        largura = int(sqrt(len(self.lista_de_cartas))) + 1
        for idx,carta in enumerate(self.lista_de_cartas):
            foto = carta['foto']
            titulo = carta['titulo']
            plt.subplot(largura,largura,idx+1),plt.imshow(foto,cmap = 'gray')
            plt.title(titulo), plt.xticks([]), plt.yticks([])
        plt.show()

