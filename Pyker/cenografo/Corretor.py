import re

class Corretor:

    def __init__(self):
        pass

    def corrigir(self,resposta,mural):
        if mural == 'diler':
            return self.regra_diler(resposta)
        elif mural == 'vez':
            return self.regra_vez(resposta)
        elif mural == 'hole_cards':
            return self.regra_hole_cards(resposta)
        elif mural == 'combo':
            return self.regra_combo(resposta)
        elif mural == 'aposta':
            return self.regra_aposta(resposta)
        elif mural == 'fichas':
            return self.regra_fichas(resposta)
        elif mural == 'pote':
            return self.regra_pote(resposta)
        elif mural == 'pote_rodada':
            return self.regra_pote_rodada(resposta)
        elif mural == 'bord':
            return self.regra_bord(resposta)

    def regra_diler(self,resposta):
        if resposta < 1000:
            return False
        else:
            return True

    def regra_vez(self,resposta):
        if resposta < 1000:
            return False
        else:
            return True

    def regra_hole_cards(self,resposta):
        if resposta < 1000:
            return False
        else:
            return True

    def regra_fichas(self,resposta):
        reposta = self.regra_filtro(resposta,30000,r'\$(\d*(\,\d{2})?)')
        reposta = str.replace(reposta,'$', '')
        reposta = str.replace(reposta,',', '.')
        reposta = "".join([reposta,'0'])
        return float(reposta)

    def regra_aposta(self,resposta):
        reposta = self.regra_filtro(resposta,30000,r'\$(\d*(\,\d{2})?)')
        reposta = str.replace(reposta,'$', '')
        reposta = str.replace(reposta,',', '.')
        reposta = "".join([reposta,'0'])
        return float(reposta)

    def regra_bord(self,resposta):
        return self.regra_filtro(resposta,6000,r'[C|P|E|O]{1}(J|Q|K|A|10|[2-9])')

    def regra_combo(self,resposta):
        return self.regra_filtro(resposta,6000,r'(J|Q|K|A|T|[2-9])[C|P|E|O]{1}')

    def regra_pote(self,resposta):
        reposta = self.regra_filtro(resposta,30000,r'\$(\d*(\,\d{2})?)')
        reposta = str.replace(reposta,'$', '')
        reposta = str.replace(reposta,',', '.')
        reposta = "".join([reposta,'0'])
        return float(reposta)

    def regra_pote_rodada(self,resposta):
        reposta = self.regra_filtro(resposta,30000,r'\$(\d*(\,\d{2})?)')
        reposta = str.replace(reposta,'$', '')
        reposta = str.replace(reposta,',', '.')
        reposta = "".join([reposta,'0'])
        return float(reposta)

    def regra_filtro(self,lista_de_caracter,erro,ER):
        palavra = ''
        indice = 0
        resposta = ''
        
        for idx,item in enumerate(lista_de_caracter):
            if item[1] < erro:
                palavra = ''.join([palavra,item[0]])
        while indice < len(palavra):
            imgtag = re.match(ER,palavra[indice:])
            if imgtag:
                resposta = imgtag.group(0)
            indice = indice + 1
        return resposta


