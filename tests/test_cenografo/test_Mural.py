import cv2
import unittest
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
import Pyker.cenografo.Mural as Mural


class MuralTest(unittest.TestCase):

    def test_inicia(self):
        print('-----------------test_inicia------------------')
        mural = Mural.Mural('texto','')
        mural.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/aposta/entrada.jpg')

    def test_adicionar_seleciona_remover_recorte(self):
        print("-----------------test_adicionar_seleciona_remover_recorte-----------------")
        caminho = {'modelo': 'MPSC6', 'mural': 'diler'}
        mural = Mural.Mural('binario',caminho)
        mural.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/aposta/entrada.jpg')
        mural.cor = (0, 255, 0)
        mural.adicionar_recorte('A', (0, 100, 0, 100))
        self.assertTrue(mural.dicionario_de_recortes.get('A'))
        self.assertTrue(mural.dicionario_das_respostas_dos_recortes.get('A'))

        caminho_recorte = {'modelo': 'MPSC6', 'mural': 'diler', 'recorte':'A'}
        self.assertEqual(mural.selecionar_recorte('A').caminho, caminho_recorte)
        self.assertEqual(mural.selecionar_resposta_do_recorte('A'), 'null')

        mural.remover_recorte('A')
        self.assertFalse(mural.selecionar_recorte('A'))
        self.assertFalse(mural.selecionar_resposta_do_recorte('A'))


    def test_show(self):
        print('-----------------test_show------------------')
        caminho = {'modelo': 'MPSC6', 'mural': 'diler'}
        mural = Mural.Mural('binario', caminho)
        mural.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_2.jpg')
        mural.adicionar_recorte('A', (131, 149, 373, 392))
        mural.adicionar_recorte('B', (209, 227, 352, 371))
        mural.adicionar_recorte('C', (231, 249, 275, 294))
        mural.adicionar_recorte('D', (209, 227, 115, 134))
        mural.adicionar_recorte('E', (128, 146, 100, 119))
        mural.adicionar_recorte('F', (95, 113, 197, 216))
        mural.show()

    def test_set_imagem(self):
        print('-----------------test_set_imagem------------------')
        caminho = {'modelo': 'MPSC6', 'mural': 'diler'}
        mural = Mural.Mural('binario', caminho)
        mural.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_2.jpg')
        mural.adicionar_recorte('A', (131, 149, 373, 392))
        mural.adicionar_recorte('B', (209, 227, 352, 371))
        mural.adicionar_recorte('C', (231, 249, 275, 294))
        mural.adicionar_recorte('D', (209, 227, 115, 134))
        mural.adicionar_recorte('E', (128, 146, 100, 119))
        mural.adicionar_recorte('F', (95, 113, 197, 216))
        mural.show()
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_2.jpg')
        mural.set_imagem(imagem)
        mural.show()

    def test_set_cor(self):
        print('-----------------test_set_cor------------------')
        caminho = {'modelo': 'MPSC6', 'mural': 'diler'}
        mural = Mural.Mural('binario', caminho)
        mural.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_2.jpg')
        mural.adicionar_recorte('A', (131, 149, 373, 392))
        mural.adicionar_recorte('B', (209, 227, 352, 371))
        mural.adicionar_recorte('C', (231, 249, 275, 294))
        mural.adicionar_recorte('D', (209, 227, 115, 134))
        mural.adicionar_recorte('E', (128, 146, 100, 119))
        mural.adicionar_recorte('F', (95, 113, 197, 216))
        mural.show()
        mural.set_cor((0, 255, 0))
        mural.show()

    def test_comparar_binario(self):
        print('-----------------test_comparar_binario------------------')
        caminho = {'modelo': 'MPSC6', 'mural': 'diler'}
        mural = Mural.Mural('binario', caminho)
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_3.jpg')
        mural.set_imagem(imagem)
        mural.adicionar_recorte('A', (131, 149, 373, 392))
        mural.adicionar_recorte('B', (209, 227, 352, 371))
        mural.adicionar_recorte('C', (231, 249, 275, 294))
        mural.adicionar_recorte('D', (209, 227, 115, 134))
        mural.adicionar_recorte('E', (128, 146, 100, 119))
        mural.adicionar_recorte('F', (95, 113, 197, 216))
        mural.show()
        print(mural.comparar())
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_2.jpg')
        mural.set_imagem(imagem)
        mural.show()
        print(mural.comparar())
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        mural.set_imagem(imagem)
        mural.show()
        print(mural.comparar())


    def test_comparar_texto(self):
        print('-----------------test_comparar_texto------------------')
        caminho = {'modelo': 'MPSC6', 'mural': 'aposta'}
        mural = Mural.Mural('texto', caminho)
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_3.jpg')
        mural.set_imagem(imagem)
        mural.adicionar_recorte('A', (116, 131, 273, 373))
        mural.adicionar_recorte('D', (115, 130, 113, 213))
        mural.adicionar_recorte('C', (209, 224, 179, 279))
        mural.adicionar_recorte('B', (192, 206, 99, 199))
        mural.adicionar_recorte('E', (192, 206, 280, 380))
        mural.adicionar_recorte('F', (95, 110, 218, 318))
        print(mural.comparar())
        mural.show()
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_4.jpg')
        mural.set_imagem(imagem)
        print(mural.comparar())
        mural.show()
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_5.jpg')
        mural.set_imagem(imagem)
        print(mural.comparar())
        mural.show()

    def test_modelo(self):
        print('-----------------test_modelo------------------')

        caminho = {'modelo': 'MPSC6', 'mural': 'aposta'}
        mural = Mural.Mural('texto', caminho)
        mural.adicionar_recorte('A', (131, 149, 373, 392))
        mural.adicionar_recorte('B', (209, 227, 352, 371))
        mural.adicionar_recorte('C', (231, 249, 275, 294))

        resposta_correta = {'aposta': {'cor': (0, 0, 0),
                                       'dado': 'texto',
                                       'recortes': {'A': (131, 149, 373, 392),
                                                    'B': (209, 227, 352, 371),
                                                    'C': (231, 249, 275, 294)}}}

        assert mural.modelo() == resposta_correta
        print(mural.modelo())


    def informacao(self):
        print
        '-----------------test_informacao------------------'
        mural = Mural()
        cor = (0, 255, 0)
        imagem = cv2.imread('cenografo/Moldes/MPSC6/Bases/teste/mesa_4.jpg')
        mural.inicia('texto', '$,0123456789', 'aposta', 'cenografo/Moldes/MPSC6/Bases/', imagem, cor)
        mural.adicionar_recorte('A', (116, 131, 273, 373))
        mural.adicionar_recorte('B', (115, 130, 113, 213))
        mural.adicionar_recorte('C', (209, 224, 179, 279))
        mural.adicionar_recorte('D', (192, 206, 99, 199))
        mural.adicionar_recorte('E', (192, 206, 280, 380))
        mural.adicionar_recorte('F', (95, 110, 218, 318))
        mural.informacao()

    def dados_binario(self):
        print
        '-----------------test_dados_binario------------------'
        mural = Mural()
        nome = 'diler'
        imagem = cv2.imread('cenografo/Moldes/MPSC6/Bases/teste/mesa_3.jpg')
        cor = (0, 255, 0)
        mural.inicia('binario', 'null', nome, 'Moldes/MPSC6/Bases/', imagem, cor)
        mural.adicionar_recorte('A', (131, 149, 373, 392))
        mural.adicionar_recorte('B', (209, 227, 352, 371))
        mural.adicionar_recorte('C', (231, 249, 275, 294))
        mural.adicionar_recorte('D', (209, 227, 115, 134))
        mural.adicionar_recorte('E', (128, 146, 100, 119))
        mural.adicionar_recorte('F', (95, 113, 197, 216))
        print
        mural.dados('teste/mesa_10_10_2018_3_11/etapa_11')

    def dados_texto(self):
        print
        '-----------------test_dados_texto------------------'
        mural = Mural()
        nome = 'aposta'
        imagem = cv2.imread('cenografo/Moldes/MPSC6/Bases/teste/mesa_3.jpg')
        cor = (0, 255, 0)
        mural.inicia('numero', '$,0123456789', nome, 'cenografo/Moldes/MPSC6/Bases/', imagem, cor)
        mural.adicionar_recorte('A', (116, 131, 273, 373))
        mural.adicionar_recorte('B', (115, 130, 113, 213))
        mural.adicionar_recorte('C', (209, 224, 179, 279))
        mural.adicionar_recorte('D', (192, 206, 99, 199))
        mural.adicionar_recorte('E', (192, 206, 280, 380))
        mural.adicionar_recorte('F', (95, 110, 218, 318))
        mural.dados('teste/mesa_10_10_2018_3_11/etapa_11')


if __name__ == "__main__":
    print('Teste da classe Mural')
    unittest.main()

