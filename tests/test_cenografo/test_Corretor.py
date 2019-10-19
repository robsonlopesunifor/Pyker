import unittest
import cv2
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
import Pyker.cenografo.Corretor as Corretor
import Pyker.cenografo.Texto as Texto

class Corretor_test(unittest.TestCase):

    def test_iniciar(self):
        pass

    def test_regra_diler(self):
        print('-------test_regra_diller--------')
        corretor = Corretor.Corretor()
        print(corretor.regra_diler(6000))

    def test_regra_filtro(self):
        print('-------test_regra_filtro--------')
        corretor = Corretor.Corretor()
        lista = []
        palavra = ',,,,,$,,,,$65,785,,,,9,,$76,980'
        for letra in palavra:
            lista.append([letra, 1100])
        print(corretor.regra_filtro(lista, 2000, r'\$(\d*(\,\d{2})?)'))

    def test_regra_aposta(self):
        print('-------test_regra_aposta--------')
        corretor = Corretor.Corretor()
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'aposta', 'recorte': 'A'}
        texto = Texto.Texto(caminho_dic)
        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/aposta/B.png')
        print(corretor.corrigir(texto.comparar(), 'aposta'))

        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/aposta/C.png')
        print(corretor.corrigir(texto.comparar(), 'aposta'))

        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/aposta/D.png')
        print(corretor.corrigir(texto.comparar(), 'aposta'))

        print(corretor.regra_aposta(self.gerar_lista(',,,,,$,,,,$65,785,,,,9,,$76,980')))
        print(corretor.regra_aposta(self.gerar_lista(',,,,,$,,,,$65,,,')))


    def test_regra_fichas(self):
        print('-------test_regra_fichas--------')
        corretor = Corretor.Corretor()
        caminho_dic = {'modelo': 'MPSC6', 'mural': 'fichas', 'recorte': 'A'}
        texto = Texto.Texto(caminho_dic)
        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/fichas/D.png')
        print(corretor.corrigir(texto.comparar(), 'fichas'))

        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/fichas/E.png')
        print(texto.comparar())
        print(corretor.corrigir(texto.comparar(), 'fichas'))
        imagem = cv2.imread('../../Moldes/MPSC6/Bases/fichas/F.png')
        print(corretor.corrigir(texto.comparar(imagem), 'fichas'))
        print(corretor.regra_aposta(self.gerar_lista(',,,,,$,,,,$65,785,,,,9,,$76,980')))
        print(corretor.regra_aposta(self.gerar_lista(',,,,,$,,,,$65,,,')))
        print(corretor.regra_aposta(self.gerar_lista(',,,,,$,,,,$65,,,')))
        # print corretor.regra_aposta(self.gerar_lista(''))


    def test_regra_bord(self):
        print('-------test_regra_bord--------')
        corretor = Corretor.Corretor()
        print(corretor.regra_bord(self.gerar_lista('CC  C6 CC 777')))
        print(corretor.regra_bord(self.gerar_lista('C66')))
        print(corretor.regra_bord(self.gerar_lista('OE66')))
        print(corretor.regra_bord(self.gerar_lista('CA')))
        print(corretor.regra_bord(self.gerar_lista('C10')))
        print(corretor.regra_bord(self.gerar_lista('OJ66')))
        print(corretor.regra_bord(self.gerar_lista('CQ')))
        print(corretor.regra_bord(self.gerar_lista('PK')))

    def test_regra_combo(self):
        print('-------test_regra_combo--------')
        corretor = Corretor.Corretor()

        caminho_dic = {'modelo': 'MPSC6', 'mural': 'combo', 'recorte': 'A'}
        texto = Texto.Texto(caminho_dic)
        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/combo/B_1_NU_201821319382.png')
        print(corretor.corrigir(texto.comparar(), 'combo'))

        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/combo/B_2_NU_2018213193817.png')
        print(texto.comparar())
        print(corretor.corrigir(texto.comparar(), 'combo'))

        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/combo/D_1_NU_2018213193738.png')
        print(texto.comparar())
        print(corretor.corrigir(texto.comparar(), 'combo'))

        texto.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/combo/D_2_NU_2018213193846.png')
        print(texto.comparar())
        print(corretor.corrigir(texto.comparar(), 'combo'))


    def gerar_lista(self, palavra):
        lista = []
        for letra in palavra:
            lista.append([letra, 0])
        return lista


if __name__ == "__main__":
    print('Teste da classe Corretor')
    unittest.main()

