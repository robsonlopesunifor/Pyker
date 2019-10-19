import cv2
import numpy as np
from matplotlib import pyplot as plt
from . import Binario as Binario
from . import Texto as Texto
from . import Corretor as Corretor
import os

class Recorte:

    def __init__(self,tipo=None,caminho=None,retangolo=None,imagem=None):
        self.caminho = caminho
        self.imagem = imagem
        self.cor = self.gerar_cor()
        self.retangulo = retangolo
        self.subimagem = None
        self.tipo = tipo

        if self.tipo == 'binario':
            self.binario = Binario.Binario(caminho)
        elif self.tipo == 'texto':
            self.texto = Texto.Texto(caminho)
        self.Corretor = Corretor.Corretor()

    def cortar(self):
        proporcao = self.imagem.shape[0] / 364.0
        x_inicial = int(self.retangulo[2] * proporcao)
        x_final = int(self.retangulo[3] * proporcao)
        y_inicial = int(self.retangulo[0] * proporcao)
        y_final = int(self.retangulo[1] * proporcao)
        self.subimagem = self.imagem[y_inicial:y_final,x_inicial:x_final]
        return self.subimagem

    def marcar(self):
        proporcao = self.imagem.shape[0] / 364.0
        x_inicial = int(self.retangulo[2] * proporcao) - 1
        x_final = int(self.retangulo[3] * proporcao)
        y_inicial = int(self.retangulo[0] * proporcao) - 1
        y_final = int(self.retangulo[1] * proporcao)
        cv2.rectangle(self.imagem,(x_inicial,y_inicial), (x_final, y_final), self.cor, 1)

    def resposta(self):
        return self.corrigir()

    def corrigir(self):
        return self.Corretor.corrigir(self.comparar(),self.caminho['mural'])

    def comparar(self):
        if self.tipo == 'binario':
            resposta = self.comparar_binario()
        elif self.tipo == 'texto':
            resposta = self.comparar_texto()
        return resposta
        

    def comparar_binario(self):
        if type(self.binario.imagem_base) == np.ndarray:
            return self.binario.comparar(self.cortar())
        else:
            print('Imagem base não existe!')
            return None

    def comparar_texto(self):
        return self.texto.comparar(self.cortar())

    def info(self):
        resposta = None
        if self.dado == 'binario':
            print(self.comparar_binario())
        else:
            resposta = self.comparar_texto()
            for idx,item in enumerate(resposta):
                print(item)
        
        
    def salvar_imagem(self):
        self.cortar()
        if self.dado == 'binario':
            self.binario.imagem_topo = self.subimagem
            self.binario.salvar_base()
            self.binario.show()
        else:
            self.texto.salvar(self.subimagem)
            self.texto.show(self.subimagem)

    def dados(self,caminho):
        caminho = "".join([caminho,'/',self.nome])
        if not os.path.isdir(caminho):
            os.makedirs(caminho)
        dados = {}
        if self.dado == 'binario':
            dados = self.dados_binario(caminho)
            dados.setdefault("tipo_de_dado","binario")
        else:
            dados = self.dados_texto(caminho)
            dados.setdefault("tipo_de_dado","texto")
        dados.setdefault("corrigido",self.corrigir())
        return dados

    """
    def dados_binario(self,camilho_salvar_imagens):
        largura = self.posicao_x_final - self.posicao_x_inicial 
        altura = self.posicao_y_final - self.posicao_y_inicial 
        self.cortar()
        if self.base_carregada == False:
            self.binario.imagem_topo = self.subimagem
            self.binario.carregar_base()
            self.base_carregada = True
            return self.binario.dados(camilho_salvar_imagens)
        else:
            self.binario.imagem_topo = self.subimagem
            return self.binario.dados(camilho_salvar_imagens)
    """

    def dados_texto(self,camilho_salvar_imagens):
        self.cortar()
        return self.texto.dados(self.subimagem,camilho_salvar_imagens)

    def gerar_cor(self):
        return (255,255,255)

    def show(self):
        plt.subplot(1, 2, 1), plt.imshow(self.subimagem, cmap='gray')
        plt.title('Subimagem'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 2, 2), plt.imshow(self.imagem, cmap='gray')
        plt.title('Imagem'), plt.xticks([]), plt.yticks([])
        plt.show()

    def modelo(self):
        dicionario_modelo = {}
        dicionario_modelo.setdefault(self.caminho['recorte'],self.retangulo)
        return dicionario_modelo

