class camera:

    def __init__(self,nome):
        self.nome = nome
        

    def filmar(self):
        print(f'{self.nome} está filmando...')
        


c1=camera('Canon')
c2=camera('Sony')
c1.filmar()

c1.filmar()
c2.filmar()

#print(c1.filmando)
#print(c2.filmando)