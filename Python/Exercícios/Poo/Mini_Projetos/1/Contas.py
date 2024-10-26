from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,agencia,conta,saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self,valor):
        ...

    def depositar(self,valor):
        self.saldo += valor
        self.Verificar(f'(Deposito: R${valor:.2f})')
    
    def Verificar(self,msg=''):
        print(f'Saldo: R${self.saldo:.2f} {msg}')

class ContaPoupanca(Conta):

    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >=0:
            self.saldo -= valor
            self.Verificar(f'(Saque R${valor:.2f})')
            return self.saldo
        
        print('\nNão foi possivel sacar o valor desejado')
        self.Verificar(f'(Saque Negado de R${valor:.2f})\n')

class ContaCorrente(Conta):

    def sacar():
        ...

if __name__ == '__main__':
    
    conta1=ContaPoupanca(111,222,450)
    conta1.depositar(50)
    conta1.sacar(500)
    conta1.sacar(5)
    