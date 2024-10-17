class Sla:

    def __init__(self,user,password):
        self.user=user
        self.password=password
    def retorno(self):
        print(f'{self.user} {self.password}')

p1=Sla('nome', 'senha')

p1.retorno()