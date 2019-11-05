import requests
import json
import redis
import cv2
import numpy as np

class Dados:

    def __init__(self,lista_de_cartas,url):
        self.lista_de_cartas = lista_de_cartas
        self.headers = {'content-type': 'application/json'}
        self.redis_conectado = redis.Redis(host='localhost', port=6379)
        self.url = url


    def salvar_cenografo(self,index):
        # inserção de dados em um serviço
        if self.lista_de_cartas[index]['nova_carta'] == True:
            self.lista_de_cartas[index]['cena_salvo'] = True
            carta = self.lista_de_cartas[index]
            response = requests.post(self.url, data=json.dumps(carta), headers=self.headers)
            print(response.status_code)

    def registrar_imagem(self,index):
        if self.lista_de_cartas[index]['nova_carta'] == True:
            foto = self.lista_de_cartas[index]['foto']
            tela = self.lista_de_cartas[index]['tela']
            data = self.lista_de_cartas[index]['data']
            data_fatiada = data.split(" ")
            data_fatiada[1] = data_fatiada[1].replace(':','-')
            data_fatiada[1] = data_fatiada[1].replace('.','-')
            data_fatiada[1] = "".join([data_fatiada[1][:-3],'000'])

            retval, buffer = cv2.imencode('.jpg', foto)
            imagem_bytes = np.array(buffer).tostring()
            imagem_dicionario = {'imagem':imagem_bytes,
                                'tela':tela,
                                'data_dia':data_fatiada[0],
                                'data_hora':data_fatiada[1]}

            self.redis_conectado.rpush('imagens_pyker',str(imagem_dicionario))
            self.lista_de_cartas[index]['foto_registrada'] = True
            self.lista_de_cartas[index]['foto'] = None
            