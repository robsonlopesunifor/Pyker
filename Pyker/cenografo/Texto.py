from imutils import contours
import numpy as np
import imutils
import cv2
from datetime import datetime
from math import sqrt
from PIL import Image
from matplotlib import pyplot as plt
import sys



class Texto(object):

    def __init__(self,caminho=None):
        self.imagem = None
        self.caminho_dic = caminho
        self.dicionario_caracter_imagem = {}
        if caminho != None:
            self.carregar_dicionario_caracter_imagem()


    def carregar_dicionario_caracter_imagem(self,caminho=None):
        self.caminho_dic = self.caminho_dic if caminho == None else caminho

        imagem_base = cv2.imread(self.caminho_str(recorte='alfabeto'))
        alfabeto = self.carregar_caracteres()
        lista_caracteres = self.separar_caracteres(alfabeto)
        limpar_imagem_base = self.limpar_imagem(imagem_base)
        lista_base = self.separar_imagens(limpar_imagem_base)
        self.dicionario_caracter_imagem = self.adicionar_caracter_a_imagem(lista_caracteres, lista_base)
        return self.dicionario_caracter_imagem

    def comparar(self,imagem=None):
        if type(imagem) == np.ndarray:
            self.imagem = imagem
        imagem_topo = self.limpar_imagem(self.imagem)
        lista_topo = self.separar_imagens(imagem_topo)
        return self.encontrar_caracteres_da_imagem(lista_topo,self.dicionario_caracter_imagem)

    def limpar_imagem(self,imagem):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        mediana = self.mediana(imagem)
        thresh_binary = None
        if self.polo(imagem) < 1:
            thresh_binary = cv2.THRESH_BINARY
        else:
            thresh_binary = cv2.THRESH_BINARY_INV
        imagem = cv2.threshold(imagem, mediana, 255, thresh_binary)[1]
        return imagem

    def separar_imagens(self,imagem):
        refCnts = cv2.findContours(imagem.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        refCnts = refCnts[0] if imutils.is_cv2() else refCnts[1]
        if len(refCnts) == 0:
            return None
        refCnts = contours.sort_contours(refCnts, method="left-to-right")[0]
        digits = []
        
        for (i, c) in enumerate(refCnts):
            (x, y, w, h) = cv2.boundingRect(c)
            roi = imagem[y:y + h, x:x + w]
            roi = cv2.resize(roi, (57, 88))
            digits.append(roi)
        return digits

    def carregar_caracteres(self):
        caminho = self.caminho_str(recorte='alfabeto',tipo_arquivo='txt')
        caracteres = open(caminho, 'r')
        texto = caracteres.readlines()
        caracteres.close()
        return texto[0]


    def separar_caracteres(self,string):
        caracteris = []
        for ch in string:
            caracteris.append(ch)
        return caracteris

    def adicionar_caracter_a_imagem(self,lista_caracteres,lista_imagens):
        lista_de_dicionarios = []
        for idx,item in enumerate(lista_imagens):
            caracter = lista_caracteres[idx]
            imagem = lista_imagens[idx]
            lista_de_dicionarios.append({'caracter':caracter, 'imagem':imagem})
        return lista_de_dicionarios

    def encontrar_caracteres_da_imagem(self,lista,lista_de_dicionarios):
        lista_resposta = []
        if lista == None:
            return ''
        for idx,item in enumerate(lista):
            lista_resposta.append(['',999999999])
            for idx2,dicionario in enumerate(lista_de_dicionarios):
                err = np.sum((item.astype("float") - dicionario['imagem'].astype("float")) ** 2)
                err /= float(item.shape[0] * item.shape[1])
                if err < lista_resposta[idx][1]:
                    lista_resposta[idx][1] = err
                    lista_resposta[idx][0] = dicionario['caracter']
        return lista_resposta

    def mediana(self,imagem):
        lista = []
        lista_hist = cv2.calcHist([imagem], [0], None, [256], [0, 256])
        for idx,item in enumerate(lista_hist):
            if idx >= 100:
                lista.append(item)
        return (90 + lista.index(max(lista)))

    def polo(self,imagem):
        polo = 0
        for idx,item in enumerate(imagem[0]):
            if item > 130:
                polo += 1
            else:
                polo -= 1
        return polo

    def salvar(self,imagem):
        imagem = self.limpar_imagem(imagem)
        caminho = self.caminho_str(True)
        Image.fromarray(imagem).save(caminho)
        return caminho

    """
    def dados(self,imagem,camilho_salvar_imagens):
        dicionario = {}
        lista = []
        size = 20, 20
        caminho_imagem = "".join([camilho_salvar_imagens,'/',self.nome,'_imagem.png'])
        Image.fromarray(imagem).save(caminho_imagem)
        dicionario.setdefault("imagem",caminho_imagem)
        imagem_limpa = self.limpar_imagem(imagem)
        caminho_imagem_limpa = "".join([camilho_salvar_imagens,'/',self.nome,'_imagem_limpa.png'])
        Image.fromarray(imagem_limpa).save(caminho_imagem_limpa)
        dicionario.setdefault("imagem_limpa",caminho_imagem_limpa)
        lista_de_imagens = self.separar_imagens(imagem_limpa) 
        lista_de_resutados = self.comparar(imagem)
        lista_imagem_resultado = []
        if lista_de_imagens != None:
            for idx,item in enumerate(lista_de_imagens):
                caminho_imagem_letra = "".join([camilho_salvar_imagens,'/',self.nome,'_letra_',str(idx),'.png'])
                Image.fromarray(cv2.resize(lista_de_imagens[idx], (15, 15))).save(caminho_imagem_letra)
                lista_imagem_resultado.append({"imagem_letra":caminho_imagem_letra,
                                               "letra_resultado":lista_de_resutados[idx]})
        dicionario.setdefault("imagem_resultado",lista_imagem_resultado)
        return dicionario
    """

    def show(self):

        imagem_limpa = self.limpar_imagem(self.imagem)
        lista_de_imagens = self.separar_imagens(imagem_limpa)
        largura = int(sqrt(len(lista_de_imagens) + 2)) + 1

        plt.subplot(largura,largura,(1)),plt.imshow(self.imagem,cmap = 'gray')
        plt.title(1), plt.xticks([]), plt.yticks([])
        plt.subplot(largura,largura,(2)),plt.imshow(imagem_limpa,cmap = 'gray')
        plt.title(2), plt.xticks([]), plt.yticks([])
        for idx,item in enumerate(lista_de_imagens):
            plt.subplot(largura,largura,(idx + 3)),plt.imshow(item,cmap = 'gray')
            plt.title(""), plt.xticks([]), plt.yticks([])
        plt.show()

    def caminho_str(self, imagem_unica=False, recorte=None, tipo_arquivo=None):
        datatime = ""
        if imagem_unica == True:
            datatime = ''.join(['_',str(datetime.now().strftime("%f"))])

        try:
            caminho_string = "/Pyker/cenografo/Moldes/"
            caminho_string = "".join([caminho_string, self.caminho_dic['modelo'], '/'])
            caminho_string = "".join([caminho_string, self.caminho_dic['mural'], '/'])
            caminho_string = "".join([caminho_string, (self.caminho_dic['recorte'] if recorte == None else recorte)])
            caminho_string = "".join([caminho_string,datatime,'.', ('png' if tipo_arquivo == None else tipo_arquivo)])
            self.caminho = sys.path[0]+caminho_string
            return self.caminho
        except:
            print('Dicionário do caminho esta errado.')
            self.caminho = ''
            return self.caminho

