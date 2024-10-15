#Codigo com objeto, sendo exportando para outro arquivo 
import json 

caminho_arquivo = 'Ex_07_c.json'

class Pessoa:
    def __init__(self, nome, sobre_nome, idade):
        self.sobre_nome=sobre_nome
        self.nome=nome 
        self.idade=idade 
    def retorno(self):
        print(f'{self.nome}{self.sobre_nome} tem {self.idade} anos')

p1=Pessoa('iderval','lima','21')
p2=Pessoa('Neto','Silva','22')
p3=Pessoa('Laila','sobras','26')
lista=[vars(p1),vars(p2),vars(p3)]

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(lista, arquivo, ensure_ascii=False, indent=2)