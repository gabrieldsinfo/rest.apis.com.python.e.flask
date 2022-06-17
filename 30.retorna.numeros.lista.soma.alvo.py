#30.RETORNA.NUMEROS.LISTA.SOMA.ALVO
#FUNCAO QUE RETORNA OS NUMEROS DA SOMA ALVO DO ARRAY OU VAZIO, CASO NENHUM DOS NUMEROS DO ARRAY SOMAREM A SOMA ALVO.

lista = [5,18,-8,2]
lista2 = lista
del lista2[0]
alvo = 10
resultado = []
for i in lista:
    for i2 in lista2:
        soma = i + i2
        if soma == alvo:
            resultado.append(i)
            resultado.append(i2)
            break
    if len(resultado) > 0:
        break
print(resultado)
