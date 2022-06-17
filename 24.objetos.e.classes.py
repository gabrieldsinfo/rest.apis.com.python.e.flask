#24.OBJETOS E CLASSES
#CLASSE = MODELO OU REPRESENTACAO DE UM OBJETO
#OBJETO = INSTANCIA DE UMA CLASSE (PODE TER FUNCOES E EXECUTAR ACOES DENTRO DELE).

"""
jogador_loteria_1 = {
    'nome': 'Pedro',
    'numeros': (13,4,52,23,67,82)
}
jogador_loteria_2 = {
    'nome': 'Pedro',
    'numeros': (13,4,52,23,67,82)
}
print(jogador_loteria_1 == jogador_loteria_2)
"""

class JogadorLoteria:
    def __init__(self): #ou
    #def __init__(self,nome):

        self.nome = "Pedro" #ou
        #self.nome = nome
        self.numeros = (13,4,52,23,67,82)

    def total(self):
        return sum(self.numeros)

jogador_1 = JogadorLoteria() 
jogador_2 = JogadorLoteria()
#ou
#jogador_1 = JogadorLoteria('Roberta')
#jogador_1 = JogadorLoteria('Felipe')

print(jogador_1.nome)
print(jogador_1.numeros)
print(jogador_1.total())

print(jogador_1 == jogador_2)
