import requests
import json

class Dados:

    def __init__(self,lista_de_cartas,url):
        self.lista_de_cartas = lista_de_cartas
        self.headers = {'content-type': 'application/json'}
        self.url = url


    def salvar_cenografo(self,index):
        # inserção de dados em um serviço
        if self.lista_de_cartas[index]['nova_carta'] == True:
            self.lista_de_cartas[index]['cena_salvo'] = True
            carta = self.lista_de_cartas[index]
            response = requests.post(self.url, data=json.dumps(carta), headers=self.headers)
            print(response.status_code)