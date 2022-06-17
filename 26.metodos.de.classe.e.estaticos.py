#26.METODOS DE CLASSE E ESTATICOS
#__INIT__ = METODO UTILIZADO PARA ATRIBUIR VALORES AOS OBJETOS.
#@CLASSMETHOD = UTILIZADO PARA CRIAR UM METODO DE UMA CLASSE QUE PODE SER CHAMADO DIRETAMENTE, SEM SER INSTANCIADO.
#@STATICMETHOD = É COMO UMA FUNÇÃO SIMPLES QUE RESIDE NO CORPO DE UMA CLASSE.
#.WEEKDAY = FUNÇÃO QUE RETORNA OS DIAS EM MÚMEROS.
#RETURN = #JÁ REALIZA A FUNÇÃO DE INTERROMPER.

class Funcionario():
    aumento = 1.04

    def __init__(self, nome, salario):
        self.nome = nome   
        self.salario = salario

    def dados (self):
        return {'nome': self.nome, 'salario': self.salario}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    @classmethod #Utilizado para criar um metodo de uma classe que pode ser chamado diretamente, sem ser instanciado.
    def definir_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento

    @staticmethod #É como uma função simples de reside no corpo de uma classe.
    def dia_util (dia):
        # segunda-feira = 0
        # terca-feira = 1
        # ...
        if dia.weekday() == 5 or dia.weekday() == 6: #função que retorna os dias em números.
            return False #return já realiza a função de interromper
        return True

fabio = Funcionario ('Fabio', 7000)
fabio.aplicar_aumento()
print(fabio.dados())

Funcionario.definir_novo_aumento(1.05)

fabio = Funcionario ('Fabio', 7000)
fabio.aplicar_aumento()
print(fabio.dados())

pedro = Funcionario ('Pedro', 8000)
pedro.aplicar_aumento()
print(pedro.dados())

import datetime
minha_data = datetime.date(2022, 5, 5) #quinta-feira
print(Funcionario.dia_util(minha_data))

