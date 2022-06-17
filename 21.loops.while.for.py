#21.LOOPS (WHILE E FOR)
#LOOPS = LACO DE REPETICAO
#WHILE = ENQUANTO
#FOR = PARA
"""
minha_variavel = "Olá"
print(len(minha_variavel))
print(minha_variavel[0])
print(minha_variavel[1])
print(minha_variavel[2])
"""

"""
minha_variavel = "Olá mundo"
for letra in minha_variavel:
    print(letra)
"""

"""
lista = [0,1,2,3,4,5,6,7,8,9,10]
print(lista)
#range(start,stop,step) #lista automatica
#start = 0 #automaticamente o start ja inicia-se com o 0
#stop = 1 #automaticamente o stop ja inicia-se com o 1
print(list(range(10+1)))
print(set(range(10+1)))
print(tuple(range(10+1)))
print(list(range(1,10,2)))
print(list(range(0,11,2)))
"""

"""
numeros_pares = list(range(0,11,2))
#print(numeros_pares)
for numero in numeros_pares: #for = para
    print(numero ** 3)
"""

"""
x = 0
while x <= 10: #while = enquanto
    print(x ** 3)
    x = x+2 #incrementar
"""

"""
x = 0
while x <= 10: #while = enquanto
    print(x ** 3)
    x += 2 #incrementar
"""

"""
usuario_quiser = True
while usuario_quiser == True:
    usuario_input = input("Quer continuar? (S/N)")
    if usuario_input == 'N':
        usuario_quiser = False
"""