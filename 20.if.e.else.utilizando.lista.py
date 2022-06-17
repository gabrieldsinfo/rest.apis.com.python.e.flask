#20.IF E ELSE UTILIZANDO LISTA
#ELSE = E SE.
"""
pessoas_conhecidas = ['João','Maria','Ana','Fabio']
pessoa = input("Entre com o nome de uma pessoa: ")
if pessoa in pessoas_conhecidas:
    print("Você conhece essa pessoa")
else:
    print("Você não conhece essa pessoa.")
"""
"""
pessoas_conhecidas = ['João','Maria','Ana','Fabio']
pessoa = input("Entre com o nome de uma pessoa: ")
if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(pessoa))
else:
    print("Você não conhece {}".format(pessoa))
"""
"""
pessoas_conhecidas = ['João','Maria','Ana','Fabio']
pessoa = input("Entre com o nome de uma pessoa: ")
if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(pessoa)) #
else:
    print("Você não conhece "+str(pessoa)) #(concatenar a string) soma e converte a variavel pessoa para string.
"""    