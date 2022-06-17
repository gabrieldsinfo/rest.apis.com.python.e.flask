#28.DECORADORES
#WRAPS = EMBRULHAR A FUNCAO
"""
import functools
def meu_decorador(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print("*****Embrulhando função no decorador*****")
        funcao()
        print("*****Fechando embrulho*****")
    return func_que_roda_funcao

@meu_decorador #CHAMAR O DECORADOR OU SEJA, EMBURALHAR A FUNCAO NO DECORADOR
def minha_funcao():
    print("Eu sou uma função!")

minha_funcao()
"""