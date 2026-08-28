class ContaBancaria:
    def __init__(self):
        self.titular = "sem nome"
        self.numero = "sem numero"
        self.__saldo = 0
    def depositar(self, valor):
        if valor >=0:
            self.__saldo+= valor
        else:
            raise ValueError('o valor deve ser positivo')
    def sacar(self, valor):
    