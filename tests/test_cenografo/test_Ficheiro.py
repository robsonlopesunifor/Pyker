import unittest
import cv2
import sys, os
sys.path.insert(0, os.path.abspath('../../'))
import Pyker.cenografo.Ficheiro as Ficheiro


class FicheiroTest(unittest.TestCase):


    def test_adicionar_seleciona_remover_mural(self):
        print('-------------test_adicionar_seleciona_remover_mural---------------')
        caminho = {'modelo':'MPSC6'}
        ficheiro = Ficheiro.Ficheiro(caminho)
        ficheiro.adicionar_mural('binario','diler')
        self.assertTrue(ficheiro.dicionario_de_murais.get('diler'))
        self.assertTrue(ficheiro.dicionario_das_respostas_dos_murais.get('diler'))
        self.assertEqual(ficheiro.selecionar_mural('diler').dado, 'binario')
        print("-------------Metodo selecionar_resposta_do_mural-------------")
        self.assertEqual(ficheiro.selecionar_resposta_do_mural('diler'), 'null')
        print("-------------Metodo deletar-------------")
        ficheiro.remover_mural('diler')
        self.assertFalse(ficheiro.selecionar_mural('diler'))
        self.assertFalse(ficheiro.selecionar_resposta_do_mural('diler'))


    def test_show(self):
        print('-------------test_show---------------')
        caminho = {'modelo': 'MPSC6'}
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        ficheiro = Ficheiro.Ficheiro(caminho,imagem=imagem)
        ficheiro.adicionar_mural('texto','aposta')
        ficheiro.selecionar_mural('aposta').adicionar_recorte('A', (139, 190, 614, 774))
        ficheiro.selecionar_mural('aposta').adicionar_recorte('B', (73, 124, 317, 472))
        ficheiro.adicionar_mural('binario','diler')
        ficheiro.selecionar_mural('diler').adicionar_recorte('A', (190, 200, 634, 734))
        ficheiro.selecionar_mural('diler').adicionar_recorte('B', (124, 134, 337, 442))
        ficheiro.show()

    def test_salvar_molde(self):
        print('-------------test_salvar_molde---------------')
        caminho = {'modelo': 'MPSC6'}
        ficheiro = Ficheiro.Ficheiro(caminho)
        ficheiro.ler_molde('dados.json')
        ficheiro.salvar_molde('teste.json')
        """
        ficheiro = Ficheiro()
        ficheiro.imagem = cv2.imread('Moldes/MPSC6/Bases/teste/mesa_3.jpg')
        ficheiro.ler_molde('Moldes/MPSC6/MPSC6.xml')
        ficheiro.show()
        nome_do_ficheiro_original = ficheiro.nome
        posicao_x_final_original = ficheiro.selecionar_mural('vilao').selecionar_recorte('A').posicao_x_final
        ficheiro.nome = 'teste do salvar molde'
        ficheiro.selecionar_mural('vilao').selecionar_recorte('A').posicao_x_final = 400
        ficheiro.salvar_molde('Moldes/MPSC6/MPSC6.xml')
        ficheiro.show()
        ficheiro.nome = nome_do_ficheiro_original
        ficheiro.selecionar_mural('vilao').selecionar_recorte('A').posicao_x_final = posicao_x_final_original
        ficheiro.salvar_molde('Moldes/MPSC6/MPSC6.xml')
        ficheiro.show()
        ficheiro.selecionar_mural('vilao').adicionar_recorte('C', (139, 190, 614, 774))
        cor_vez = (255, 0, 0)
        ficheiro.adicionar_mural('null', 'null', 'vez', cor_vez)
        ficheiro.selecionar_mural('vez').adicionar_recorte('A', (73, 124, 317, 472))
        ficheiro.salvar_molde('Moldes/MPSC6/MPSC6.xml')
        ficheiro.show()
        """

    def test_ler_molde(self):
        print('-------------test_ler_molde---------------')
        caminho = {'modelo': 'MPSC6'}
        ficheiro = Ficheiro.Ficheiro(caminho)
        ficheiro.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        ficheiro.ler_molde('dados.json')
        ficheiro.show()

    def test_modelo(self):
        print('-------------test_modelo---------------')
        caminho = {'modelo': 'MPSC6'}
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        ficheiro = Ficheiro.Ficheiro(caminho, imagem)
        ficheiro.dimensoes = {"largura":2000,"altura":3000}
        ficheiro.info = {"site":"","jogo":"","cadeiras":"","valor":""}
        ficheiro.adicionar_mural('binario', 'diler')
        ficheiro.adicionar_mural('binario', 'vez')
        print(ficheiro.modelo())

    def test_iniciar(self):
        print('-------------test_iniciar---------------')
        caminho = {'modelo': 'MPSC6'}
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        ficheiro = Ficheiro.Ficheiro(caminho, imagem)


    def test_set_imagem(self):
        print('-------------test_set_imagem---------------')
        caminho = {'modelo': 'MPSC6'}
        ficheiro = Ficheiro.Ficheiro(caminho)
        ficheiro.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        ficheiro.ler_molde('dados.json')
        ficheiro.show()
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_2.jpg')
        ficheiro.set_imagem(imagem)
        ficheiro.show()
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_3.jpg')
        ficheiro.set_imagem(imagem)
        ficheiro.show()


    def test_comparar(self):
        print('-------------test_comparar---------------')
        caminho = {'modelo': 'MPSC6'}
        ficheiro = Ficheiro.Ficheiro(caminho)
        ficheiro.imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_1.jpg')
        ficheiro.ler_molde('dados.json')
        print(ficheiro.comparar())
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_2.jpg')
        ficheiro.set_imagem(imagem)
        print(ficheiro.comparar())
        imagem = cv2.imread(sys.path[0] + '/Pyker/cenografo/Moldes/MPSC6/teste/mesa_3.jpg')
        ficheiro.set_imagem(imagem)
        print(ficheiro.comparar())

    def test_caminho_str(self):
        print('-------------test_caminho_str---------------')
        caminho = {'modelo': 'MPSC6'}
        ficheiro = Ficheiro.Ficheiro(caminho)
        print(ficheiro.caminho_str())

    def dados(self):
        print('-------------test_dados---------------')
        ficheiro = Ficheiro()
        ficheiro.imagem = cv2.imread(
            'G:/Meu Drive/DA  Ferramentas/Projetos/Poker/Tarefa/Analista/Analista_imagem/Arquivos_imagem/mesa_11_etapa_6.png')
        ficheiro.iniciar('Moldes/MPSC6')
        print(ficheiro.dados('teste/mesa_10_10_2018_3_11/etapa_11'))

    def informacao(self):
        print('-------------test_informacao---------------')
        ficheiro = Ficheiro()
        ficheiro.imagem = cv2.imread('Moldes/MPSC6/Bases/teste/mesa_4.jpg')
        ficheiro.iniciar('Moldes/MPSC6')
        print(ficheiro.informacao())
        ficheiro.show()


if __name__ == "__main__":
    print('____Teste da classe Ficheiro')
    unittest.main()