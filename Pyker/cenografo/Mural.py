import cv2
from . import Recorte as Recorte

class Mural:
    
    def __init__(self,dado=None,caminho=None,imagem=None):
        self.dado = dado
        self.cor = (0,0,0)
        self.caminho = caminho
        self.imagem = imagem
        self.dicionario_de_recortes = {}
        self.dicionario_das_respostas_dos_recortes = {}

    def adicionar_recorte(self,nome_do_recorte,retangulo):
        caminho = self.caminho.copy()
        caminho.setdefault('recorte',nome_do_recorte)
        novo_recorte = Recorte.Recorte(self.dado,caminho,retangulo,self.imagem)
        novo_recorte.imagem = self.imagem
        self.dicionario_de_recortes.setdefault(nome_do_recorte,novo_recorte)
        self.dicionario_das_respostas_dos_recortes.setdefault(nome_do_recorte,'null')

    def selecionar_recorte(self,nome_do_recorte):
        return self.dicionario_de_recortes.get(nome_do_recorte)

    def selecionar_resposta_do_recorte(self,nome_do_recorte):
        return self.dicionario_das_respostas_dos_recortes.get(nome_do_recorte)

    def remover_recorte(self,nome_do_recorte):
        self.dicionario_de_recortes.pop(nome_do_recorte)
        self.dicionario_das_respostas_dos_recortes.pop(nome_do_recorte)

    def marcar(self):
        for chave in self.dicionario_de_recortes:
            self.dicionario_de_recortes[chave].marcar()

    def set_imagem(self,imagem):
        self.imagem = imagem
        for chave in self.dicionario_de_recortes:
            self.dicionario_de_recortes[chave].imagem = imagem

    def set_cor(self,cor):
        self.cor = cor
        for chave in self.dicionario_de_recortes:
            self.dicionario_de_recortes[chave].cor = cor

    def comparar(self):
        for chave in self.dicionario_de_recortes:
            resposta = self.dicionario_de_recortes[chave].resposta()
            self.dicionario_das_respostas_dos_recortes[chave] = resposta
        return self.dicionario_das_respostas_dos_recortes

    """
    def dados(self,caminho):
        caminho_novo = "".join([caminho,'/',self.nome])
        if not os.path.isdir(caminho_novo):
            os.makedirs(caminho_novo)
        for chave in self.dicionario_de_recortes:
            dados = self.dicionario_de_recortes[chave].dados(caminho_novo)
            self.dicionario_das_respostas_dos_recortes[chave] = dados
        return self.dicionario_das_respostas_dos_recortes

    def informacao(self):
        resposta = self.comparar()
        for chave in resposta:
            print(chave, resposta[chave])
    """

    def show(self):
        self.marcar()
        cv2.imshow(self.caminho['mural'],self.imagem)
        cv2.waitKey(0)

    def modelo(self):
        dicionario_mural = {self.caminho['mural']:{"cor":self.cor,"dado":self.dado,"recortes":{}}}
        for recorte in self.dicionario_de_recortes:
            modelo_recorte = self.selecionar_recorte(recorte).modelo()
            dicionario_mural[self.caminho['mural']]['recortes'].update(modelo_recorte)
        return dicionario_mural