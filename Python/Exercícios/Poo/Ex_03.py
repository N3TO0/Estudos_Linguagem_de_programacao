class animal:
    #nome='Leão'
    def __init__(self,nome):
        self.nome=nome
        var='valor'
    def sla(self, *args, **kwargs):
        print(*args)
        for item,itemm in kwargs.items():
            print(item,itemm)

leão=animal(nome ='leão')
print(leão.sla(22,3,4,5,nome='neto',nome2='luiza'))

#print(animal.nome)

#------------------------------------------------
