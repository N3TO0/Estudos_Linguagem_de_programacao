class sla:
    def __init__(self,nome,idade,sobre_nome):
        self.nome=nome
        self.idade=idade
        self.sobre_nome=sobre_nome
    def retorno(self,*args,**kwargs ):

        print(f'\n{self.nome} {self.sobre_nome} tem {self.idade} anos!\n')

        print(f'\n',args,'\n')

        for chave, valor in kwargs.items():
            print(chave, valor,end='\n')

p1=sla('neto', 22, 'silva')

p1.retorno(1,2,3,4,5,22,44,nome2='tadeu1', nome4='tadeu', numero=22)
