# -*- coding: cp1252 -*-
import cv2
import json
import sys
from . import Mural as Mural


class Ficheiro(object):
    
    def __init__(self,caminho={},imagem=None):
        self.molde_json = 'null'
        self.imagem = imagem
        self.dimensoes = {"largura":2000,"altura":3000}
        self.info = {"site":"","jogo":"","cadeiras":"","valor":""}
        self.caminho = caminho

        self.dicionario_de_murais = {}
        self.dicionario_das_respostas_dos_murais = {}

    def adicionar_mural(self,dado,nome_do_mural):
        caminho = self.caminho.copy()
        caminho.setdefault('mural', nome_do_mural)
        novo_mural = Mural.Mural(dado,caminho,self.imagem)
        self.dicionario_de_murais.setdefault(nome_do_mural,novo_mural)
        self.dicionario_das_respostas_dos_murais.setdefault(nome_do_mural,'null')

    def selecionar_mural(self,nome_do_mural):
        return self.dicionario_de_murais.get(nome_do_mural)

    def selecionar_resposta_do_mural(self,nome_do_mural):
        return self.dicionario_das_respostas_dos_murais.get(nome_do_mural)

    def remover_mural(self,nome_do_mural):
        self.dicionario_de_murais.pop(nome_do_mural)
        self.dicionario_das_respostas_dos_murais.pop(nome_do_mural)

    def salvar_molde(self,arquivo="modelo.json"):
        data = self.modelo()
        caminho = self.caminho_str() + arquivo
        with open(caminho, 'w') as outfile:
            json.dump(data, outfile)


    def ler_molde(self,arquivo="modelo.json"):
        caminho = self.caminho_str() + arquivo
        with open(caminho,'r') as data_file:
            data = json.load(data_file)

        murais = data['murais']
        for mural in murais:
            dado = murais[mural]['dado']
            self.adicionar_mural(dado,mural)
            recortes = data['murais'][mural]['recortes']
            for recorte in recortes:
                dimencoes = recortes[recorte]
                self.selecionar_mural(mural).adicionar_recorte(recorte,dimencoes)

    def modelo(self):
        dicionario_fichario = {'info': self.info, 'dimensoes': self.dimensoes, "murais": {}}
        for mural in self.dicionario_de_murais:
            modelo_mural = self.dicionario_de_murais[mural].modelo()
            dicionario_fichario['murais'].update(modelo_mural)
        return dicionario_fichario

    def marcar(self):
        for chave in self.dicionario_de_murais:
            self.dicionario_de_murais[chave].marcar()

    def set_imagem(self,imagem):
        self.imagem = imagem
        for chave in self.dicionario_de_murais:
            self.dicionario_de_murais[chave].set_imagem(imagem)

    def comparar(self):
        for chave in self.dicionario_de_murais:
            murais = self.dicionario_de_murais[chave]
            self.dicionario_das_respostas_dos_murais[chave] = murais.comparar()
        return self.dicionario_das_respostas_dos_murais

    """
    def dados(self,caminho):
        if not os.path.isdir(caminho):
            os.makedirs(caminho)
        for chave in self.dicionario_de_murais:
            murais = self.dicionario_de_murais[chave].dados(caminho)
            self.dicionario_das_respostas_dos_murais[chave] = murais
        
        json.dump(self.dicionario_das_respostas_dos_murais,open("".join([caminho,'/ficheiro.json']), 'w'))

        imagem = cv2.cvtColor(self.imagem, cv2.COLOR_RGB2BGR) 
        Image.fromarray(imagem).save("".join([caminho,'/imagem.png']))
        return self.dicionario_das_respostas_dos_murais
    """

    """
    def informacao(self):
        fichario = self.comparar()
        for chave_mural in fichario:
            print('---', chave_mural)
            if type(fichario[chave_mural]) is dict:
                for chave_recorte in fichario[chave_mural]:
                    print('------',chave_recorte,'---', fichario[chave_mural][chave_recorte])
            else:
                print('------',chave_recorte,'---', fichario[chave_mural])
    """

    def show(self):
        self.marcar()
        cv2.imshow('ficheiro',self.imagem)
        cv2.waitKey(0)        

    def caminho_str(self):
        try:
            caminho_string = "/Pyker/cenografo/Moldes/"
            caminho_string = "".join([caminho_string, self.caminho['modelo'], '/'])
            return sys.path[0]+caminho_string
        except:
            print('Dicionário do caminho esta errado.')
            return ''


