import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import sys


class Binario(object):

    def __init__(self,caminho=None):
        self.imagem_base = None
        self.imagem_topo = None
        self.caminho_dic = caminho
        self.caminho = 'null'
        if caminho != None:
            self.caminho_str()
            self.carregar_base()

    def carregar_base(self):
        self.imagem_base = cv2.imread(self.caminho, cv2.COLOR_RGB2BGR)
        return self.imagem_base

    def salvar_base(self):
        imagem = cv2.cvtColor(self.imagem_topo, cv2.COLOR_RGB2BGR)
        Image.fromarray(imagem).save(self.caminho)
        return self.carregar_base()
        
    def comparar(self,imagem_topo=None):
        if type(imagem_topo) == np.ndarray:
            self.imagem_topo = imagem_topo
        imageA = cv2.cvtColor(self.imagem_base, cv2.COLOR_BGR2GRAY)
        imageB = cv2.resize(self.imagem_topo,(imageA.shape[1], imageA.shape[0]),interpolation = cv2.INTER_AREA)
        imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        return err

    def show(self):
        plt.subplot(1,2,1),plt.imshow(self.imagem_topo,cmap = 'gray')
        plt.title('Imagem topo'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(self.imagem_base,cmap = 'gray')
        plt.title('Imagem base'), plt.xticks([]), plt.yticks([])
        plt.show()

    def caminho_str(self):
        try:
            caminho_string = "/Pyker/cenografo/Moldes/"
            caminho_string = "".join([caminho_string, self.caminho_dic['modelo'], '/'])
            caminho_string = "".join([caminho_string, self.caminho_dic['mural'], '/'])
            caminho_string = "".join([caminho_string, self.caminho_dic['recorte'], ".png"])
            self.caminho = sys.path[0]+caminho_string
            return self.caminho
        except:
            print('Dicionário do caminho esta errado.')
            self.caminho = ''
            return self.caminho
