#22.COMPREENSAO DE LISTA
#RANGE = SEQUENCIA
"""
print([x for x in range(5)])
print([x ** 2 for x in range(5)])
print([x ** 3 for x in range(5)])
print([x + 10 for x in range(5)])
"""

"""
print(list(range(0,10,2)))
print(10 % 3) #resto
print(1 % 2)
print([n for n in range(11) if n % 2 == 1]) #lista os numeros impares
print([n for n in range(11) if n % 2 == 0]) #lista os numeros pares
"""

"""
pessoas = ['Ana ', 'manuela', 'FELIPe ', 'Pedr0 ']
ana = ' Ana'
print(ana)
print(ana.strip()) #retira os espacos
print(ana.lower()) #modifica para letras minusculas
print(ana.upper()) #modifica para letras maiusculas
print(ana.capitalize()) #modifica a primeira letra para maiuscula
print(ana.strip().upper()) #neste caso configuramos para retirar os espacos e modificar todo os caracteres para maiusculo
pessoas_normalizadas = [pessoa.strip().upper() for pessoa in pessoas]
print(pessoas_normalizadas)
"""