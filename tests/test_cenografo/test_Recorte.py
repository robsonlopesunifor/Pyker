import cv2
import unittest
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
import Pyker.cenografo.Recorte as Recorte

class RecorteTest(unittest.TestCase):

    def test_cortar(self):
        print('--------------test_cortar--------------')
        recorte = Recorte.Recorte()
        recorte.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/entrada.jpg')
        recorte.retangulo = (0, 100, 0, 100)
        recorte.cortar()
        cv2.imshow('teste do metodo cortar' ,recorte.subimagem)
        cv2.waitKey(0)

    def test_marcar(self):
        print('--------------test_marcar--------------')
        recorte = Recorte.Recorte()
        recorte.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/entrada.jpg')
        recorte.retangulo = (0,100,0,100)
        recorte.marcar()
        cv2.imshow('teste do metodo marca' ,recorte.imagem)
        cv2.waitKey(0)

    def test_inicia(self):
        print('--------------test_inicia--------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'Diler', 'recorte': 'A'}
        retangulo = (209, 352, 226, 370)
        tipo = 'binario'

        recorte = Recorte.Recorte(tipo, caminho_dic, retangulo)
        recorte.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/entrada.jpg')
        print(recorte.comparar_binario())

    def test_show(self):
        print('--------------test_show--------------')
        recorte = Recorte.Recorte()
        recorte.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/entrada.jpg')
        recorte.retangulo = (0, 100, 0, 100)
        recorte.marcar()
        recorte.cortar()
        recorte.show()

    def test_comparar_binario(self):
        print('--------------test_comparar_binario--------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'Diler', 'recorte': 'A'}
        retangulo = (209, 352, 226, 370)
        recorte = Recorte.Recorte('binario',caminho_dic,retangulo)
        recorte.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/entrada.jpg')
        print(recorte.comparar_binario())

    def test_comparar_texto(self):
        print('--------------test_comparar_texto--------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'alfabeto'}
        retangulo = (116 ,131 ,273 ,373)
        dados = {'tipo_de_recorte': 'texto',
                 'tipo_de_texto': 'numerico',
                 'alfabeto': '$.0123456789', }
        recorte = Recorte.Recorte('texto',caminho_dic, retangulo)
        recorte.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/mesa_3.jpg')
        print(recorte.comparar_texto())

    def test_comparar(self):
        print('--------------test_comparar--------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'alfabeto'}
        retangulo = (116 ,131 ,273 ,373)
        recorte = Recorte.Recorte('texto',caminho_dic, retangulo)
        recorte.imagem = cv2.imread(sys.path[0]+'/Pyker/cenografo/Moldes/MPSC6/teste/mesa_3.jpg')
        print(recorte.comparar())

    def test_corrigir(self):
        print('--------------test_corrigir--------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'A'}
        retangulo = (273, 373,116, 131)
        recorte = Recorte.Recorte('texto', caminho_dic, retangulo)
        recorte.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_4.jpg')
        recorte.marcar()
        recorte.cortar()
        print(recorte.corrigir())
        recorte.show()

    def dados_binario(self):
        print('--------------test_dados_binario--------------')
        nome = 'B'
        imagem = cv2.imread('cenografo/Moldes/MPSC6/Bases/teste/entrada.jpg')
        cor = (255 ,255 ,0)
        retangulo = (209 ,226 ,352 ,370)
        recorte = Recorte()
        recorte.inicia('binario' ,'' ,nome ,'cenografo/Moldes/MPSC6/Bases/diler/' ,imagem ,cor ,retangulo)
        print(recorte.dados('teste/mesa_10_10_2018_3_11/etapa_11/diler/'))

    def dados_texto(self):
        print('--------------test_dados_texto--------------')
        nome = 'B'
        imagem = cv2.imread('cenografo/Moldes/MPSC6/Bases/teste/mesa_3.jpg')
        cor = (255 ,255 ,0)
        retangulo = (116 ,131 ,273 ,373)
        recorte = Recorte()
        recorte.inicia('numero' ,'$,0123456789' ,nome ,'cenografo/Moldes/MPSC6/Bases/aposta/' ,imagem ,cor ,retangulo)
        print(recorte.dados('teste/mesa_10_10_2018_3_11/etapa_11/aposta/'))

    def test_modelo(self):
        print('--------------test_modelo--------------')
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'A'}
        retangulo = (273, 373, 116, 131)
        recorte = Recorte.Recorte('texto', caminho_dic, retangulo)
        print(recorte.modelo())
        assert recorte.modelo() == {'A':(273, 373, 116, 131)}


if __name__ == "__main__":
    print('Teste da classe Recorte')
    unittest.main()