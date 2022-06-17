#27.*ARGS E **KWARGS
#*ARGS = ARGUMENTOS
#**KWARGS = ARGUMENTOS DE PALVRAS-CHAVE
"""
def meu_metodo(arg1,arg2):
    return arg1 + arg2
print(meu_metodo(5,6))

def meu_metodo_longo(arg1,arg2,arg3,arg4,arg5):
    return arg1 ++ arg2 + arg3 + arg4 + arg5
print(meu_metodo_longo(2,4,5,7,2))
"""
#MELHOR PRATICA OU SOLUCAO:
"""
def minha_lista_somada(lista):
    return sum(lista)
print(minha_lista_somada([3,6,7,3,2]))

def soma_simplificada(*args):
    return sum(args)
print(soma_simplificada(6,3,5,7,4))

def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
metodo_kwargs(3,'saa',4,'qualquer',nome='Ana', idade=25) #OBS: COLOCAR O ARGS ANTES DO KWARGS
"""