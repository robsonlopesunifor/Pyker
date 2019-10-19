import random
import pandas as pd
import json

class Auxiliar(object):


    def retornar_lista_telas_embaralhadas(self,tamanho,telas):
        quadros_por_tela = {}
        telas_embaralhadas = []

        for telas in range(1,telas+1):
            quadros_por_tela.setdefault(telas,0)

        while True:
            if len(telas_embaralhadas) >= (tamanho*telas):
                break
            else:
                valor = random.randint(1,telas)
                if quadros_por_tela[valor] < tamanho:
                    telas_embaralhadas.append((valor,quadros_por_tela[valor]))
                    quadros_por_tela[valor] += 1

        return telas_embaralhadas

    def reparar_dicionario_com_telas_embaralhadas(self,dataframe,objeto_reparar,tamanho,telas):

        index = 0
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(tamanho, telas)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe.loc[index] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe.loc[index, (chave)] = novo_ficheiro[chave]
            objeto_reparar.reparar(index)
            index += 1
            while True:
                if len(dataframe) == index:
                    break
                objeto_reparar.reparar(index)
                index += 1

    def analizar_dicionario_com_telas_embaralhadas(self,dataframe,objeto_reparar,tamanho,telas):
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(tamanho, telas)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            dataframe.loc[idx] = False
            novo_ficheiro = self.gerador_de_ficheiros(tupla[1])
            novo_ficheiro.setdefault('tela', tupla[0])
            for chave in novo_ficheiro:
                dataframe.loc[idx, (chave)] = novo_ficheiro[chave]
            objeto_reparar.analizar(idx)


    def embaralhar_dataframe(self,csv,telas):
        df_embaralhado = pd.DataFrame()
        df = pd.read_csv(csv, sep=';')
        lista_telas_embaralhadas = self.retornar_lista_telas_embaralhadas(len(df),telas)
        for idx, tupla in enumerate(lista_telas_embaralhadas):
            serie = df.iloc[tupla[1]].copy()
            serie['tela'] = tupla[0]
            #serie['linha'] = 'null'
            df_embaralhado = df_embaralhado.append(serie, ignore_index=True)
        return df_embaralhado

    def gerador_de_ficheiros(self,novo_ficheiro):
        pass

    def embaralhar_ficheiro(self):
        print('------------- adicionar_ficheiro_a_tabela ---------------')
        file = open('ficheiro.json')
        ficheiros = json.load(file)
        file.close()

        for ficheiro in ficheiros:
            print(ficheiro)
