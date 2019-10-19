import cv2
import numpy as np
import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../../Pyker'))
import cenografo.Binario as Binario


class BinarioTest(unittest.TestCase):

    def test_camino_str(self):
        # Dicionario do caminho correto
        binario = Binario.Binario()
        binario.caminho_dic = {'modelo': 'MPSC6', 'mural': 'Diler', 'recorte': 'A'}
        assert binario.caminho_str() == sys.path[0]+'/Pyker/Moldes/MPSC6/Diler/A.png'
        # Dicionario do caminho errado
        binario.caminho_dic = None
        assert binario.caminho_str() == ''

    def test_carregar_base(self):
        print('================[ test_carregar_base ]================')
        # 1° caminho certo. Acha a imagem.
        binario = Binario.Binario()
        binario.caminho_dic = {'modelo':'MPSC6','mural':'teste','recorte':'A'}
        binario.caminho_str()
        assert type(binario.carregar_base()) == np.ndarray
        # 2° caminho errado. Não acha a imagem.
        binario = Binario.Binario()
        binario.caminho_dic = {'modelo': '', 'mural': 'teste', 'recorte': 'A'}
        binario.caminho_str()
        assert binario.carregar_base() == None
        # 3° caminho não existe.
        binario = Binario.Binario()
        binario.caminho_str()
        assert binario.carregar_base() == None


    def test_salvar_base(self):
        print('================[  test_salvar_base  ]===============')
        binario = Binario.Binario()
        binario.imagem_topo = cv2.imread(sys.path[0]+"/Pyker/Moldes/MPSC6/teste/teste.png")
        binario.caminho_dic = {'modelo': 'MPSC6', 'mural': 'teste', 'recorte': 'teste'}
        caminho = binario.caminho_str()
        os.remove(caminho)
        binario.salvar_base()
        assert type(binario.imagem_base) == np.ndarray


    def test_comparar(self):
        print('===============================[ test_comparar ]===============================')
        binario = Binario.Binario()
        binario.imagem_base = cv2.imread(sys.path[0]+"/Pyker/Moldes/MPSC6/teste/vez_topo.jpg")
        binario.imagem_topo = cv2.imread(sys.path[0]+"/Pyker/Moldes/MPSC6/teste/vez_topo.jpg")
        assert binario.comparar() == 0.0
        binario.imagem_base = cv2.imread(sys.path[0]+"/Pyker/Moldes/MPSC6/teste/vez_base.jpg")
        imagem_topo = cv2.imread(sys.path[0]+"/Pyker/Moldes/MPSC6/teste/vez_topo.jpg")
        assert binario.comparar(imagem_topo) == 10030.89552238806

    def test_show(self):
        print('===============================[ test_show ]===============================')
        binario = Binario.Binario()
        binario.imagem_topo = cv2.imread(sys.path[0]+"/Pyker/Moldes/MPSC6/teste/vez_topo.jpg")
        binario.imagem_base = cv2.imread(sys.path[0]+"/Pyker/Moldes/MPSC6/teste/vez_topo.jpg")
        binario.show()

    def test_iniciar(self):
        print('===============================[ test_iniciar ]===============================')
        binario1 = Binario.Binario()
        assert binario1.imagem_base == None
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'teste', 'recorte': 'A'}
        binario2 = Binario.Binario(caminho_dic)
        assert type(binario2.imagem_base) == np.ndarray


    def dados(self):
        print('===============================[ test_dados ]===============================')
        binario = Binario.Binario()
        binario.iniciar("Moldes/MPSC6/Bases/vez/","A")
        binario.imagem_topo = cv2.imread("Moldes/MPSC6/Bases/teste/vez_topo.jpg")
        print(binario.dados('teste/mesa_10_10_2018_3_11/etapa_11/vez'))

if __name__ == "__main__":
    print('____Teste da classe binario')
    unittest.main()
