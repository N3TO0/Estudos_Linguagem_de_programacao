class pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome=nome
        self.idade=idade
        self.sexo=sexo

    def retorno1 (self):
        print(f'\n{self.nome} tem a idade: {self.idade} e sua sexualidiade é: {self.sexo}')

    def mais18 (self):
        print(f'\n{self.nome} é maior de idade pois tem: {self.idade} anos') if self.idade >= 18 else print(f'\n{self.nome} é menor de idade pois tem: {self.idade} anos\n')
            

p1=pessoa('Neto',22,'hetero')
p2=pessoa('clara',25,'gay')
p3=pessoa('luana',17,'bisexual')

p1.retorno1()
p2.retorno1()
p3.retorno1()

p1.mais18()
p2.mais18()
p3.mais18()

