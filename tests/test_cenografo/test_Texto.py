import cv2
import unittest
import sys, os
from matplotlib import pyplot as plt
from math import sqrt
sys.path.insert(0, os.path.abspath('../../'))
import Pyker.cenografo.Texto as Texto

class TextoTest(unittest.TestCase):

    def test_endereco(self):
        print(sys.path[0],'/Pyker/cenografo/Moldes/MPSC6/alfabeto/$09.png')

    def test_limpar_imagem(self):
        print('----------------test_limpar_imagem----------------')
        texto = Texto.Texto()

        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/alfabeto/$09.png')
        imagem = texto.limpar_imagem(imagem)
        plt.subplot(3, 2, (1)), plt.imshow(imagem, cmap='gray')
        plt.title(1), plt.xticks([]), plt.yticks([])
        #---------------------------
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/B.png')
        imagem = texto.limpar_imagem(imagem)
        plt.subplot(3, 2, (2)), plt.imshow(imagem, cmap='gray')
        plt.title(2), plt.xticks([]), plt.yticks([])
        # ---------------------------
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/C.png')
        imagem = texto.limpar_imagem(imagem)
        plt.subplot(3, 2, (3)), plt.imshow(imagem, cmap='gray')
        plt.title(3), plt.xticks([]), plt.yticks([])
        # ---------------------------
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/D.png')
        imagem = texto.limpar_imagem(imagem)
        plt.subplot(3, 2, (4)), plt.imshow(imagem, cmap='gray')
        plt.title(4), plt.xticks([]), plt.yticks([])
        # ---------------------------
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/alfabeto.png')
        imagem = texto.limpar_imagem(imagem)
        plt.subplot(3, 2, (5)), plt.imshow(imagem, cmap='gray')
        plt.title(5), plt.xticks([]), plt.yticks([])
        plt.show()


    def test_separar_imagens(self):
        print('----------------test_separar_imagens----------------')
        texto = Texto.Texto()
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/alfabeto.png')
        imagem = texto.limpar_imagem(imagem)
        lista_imagens = texto.separar_imagens(imagem)
        largura = int(sqrt(len(lista_imagens))) + 1
        for idx,item in enumerate(lista_imagens):
            plt.subplot(largura,largura,(idx + 1)),plt.imshow(item,cmap = 'gray')
            plt.title(""), plt.xticks([]), plt.yticks([])
        plt.show()

    def test_separar_caracteres(self):
        print('----------------test_separar_caracteres----------------')
        texto = Texto.Texto()
        print(texto.separar_caracteres('$17,43'))

    def test_adicionar_caracter_a_imagem(self):
        print('----------------test_adicionar_caracter_a_imagem----------------')
        texto = Texto.Texto()
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/A.png')
        imagem = texto.limpar_imagem(imagem)
        lista_imagens = texto.separar_imagens(imagem)
        lista_caracteres = texto.separar_caracteres('$17,43')
        lista_de_dicionarios = texto.adicionar_caracter_a_imagem(lista_caracteres, lista_imagens)
        largura = int(sqrt(len(lista_imagens))) + 1
        for idx,dicionario in enumerate(lista_de_dicionarios):
            plt.subplot(largura, largura, idx+1), plt.imshow(dicionario['imagem'], cmap='gray')
            plt.title(dicionario['caracter']), plt.xticks([]), plt.yticks([])
        plt.show()

    def test_encontrar_caracteres_da_imagem(self):
        print('----------------test_encontrar_caracteres_da_imagem----------------')
        texto = Texto.Texto()
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/C.png')
        imagem = texto.limpar_imagem(imagem)
        lista_imagens = texto.separar_imagens(imagem)
        lista_caracteres = texto.separar_caracteres('$17,43')
        dicionario = texto.adicionar_caracter_a_imagem(lista_caracteres, lista_imagens)
        resposta = texto.encontrar_caracteres_da_imagem(lista_imagens,dicionario)
        print(resposta)

    def test_mediana(self):
        print('----------------test_mediana----------------')
        texto = Texto.Texto()
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/A.png')
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        assert texto.mediana(imagem) == 214
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/B.png')
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        assert texto.mediana(imagem) == 245
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/C.png')
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        assert texto.mediana(imagem) == 214

    def test_caminho_str(self):
        print('----------------test_caminho_str----------------')
        texto = Texto.Texto()
        texto.caminho_dic = {'modelo': 'MPSC6', 'mural': 'teste', 'recorte': 'A'}
        print(texto.caminho_str())
        print(texto.caminho_str(True))
        print(texto.caminho_str(recorte='alfabeto'))
        print(texto.caminho_str(recorte='alfabeto',tipo_arquivo='txt'))

    def test_comparar(self):
        print('----------------test_comparar----------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'alfabeto'}
        texto = Texto.Texto(caminho_dic)
        texto.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/B.png')
        print(texto.comparar())
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/C.png')
        print(texto.comparar(imagem))
        texto.show()

    def test_carregar_dicionario_caracter_imagem(self):
        print('----------------test_carregar_dicionario_caracter_imagem----------------')
        texto = Texto.Texto()
        texto.caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'B'}
        lista_de_dicionarios = texto.carregar_dicionario_caracter_imagem()
        largura = int(sqrt(len(lista_de_dicionarios))) + 1
        for idx,dicionario in enumerate(lista_de_dicionarios):
            plt.subplot(largura, largura, idx+1), plt.imshow(dicionario['imagem'], cmap='gray')
            plt.title(dicionario['caracter']), plt.xticks([]), plt.yticks([])
        plt.show()

    def test_iniciar(self):
        print('----------------test_iniciar----------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'alfabeto'}
        texto = Texto.Texto(caminho_dic)
        texto.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/C.png')
        print(texto.comparar())


    def test_salvar(self):
        print('---------------- test_salvar ----------------')
        texto = Texto.Texto()
        texto.caminho_dic = {'modelo': 'MPSC6', 'mural': 'teste', 'recorte': 'B'}
        texto.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/C.png')
        caminho_imagem = texto.salvar(texto.imagem)
        cv2.imread(caminho_imagem)


    def test_show(self):
        print('---------------- test_show ----------------')
        texto = Texto.Texto()
        imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/aposta/B.png')
        texto.imagem = imagem
        texto.show()

    def test_carregar_caracteres(self):
        print('---------------- test_carregar_caracteres ----------------')
        texto = Texto.Texto()
        texto.caminho_dic = {'modelo': 'MPSC6', 'mural': 'bord', 'recorte': 'B'}
        print(texto.carregar_caracteres())

if __name__ == "__main__":
    print('____Teste da classe Texto')
    unittest.main()
