class Camera:
    def __init__(self, nome, gravando = False, ligado=False, foto=False): 
        self.nome = nome        
        self.gravando = gravando  
        self.ligado= ligado
        self.foto=foto

    def Botão_ligar(self):
        if self.ligado:
            print(f'{self.nome} Desligou!!')
            self.ligado=False
            self.gravando=False
           
        else:
            print(f'{self.nome} Liguou!!')
            self.ligado=True
        

    def Botão_gravar(self):

        if not self.ligado:
            return print(f'{self.nome} Não Pode Grava Pois Está Desligado!')
            

        if self.gravando:
            print(f'{self.nome} Já Está Gravando')
        
        else: 
            print(f'{self.nome} Iniciou A Gravar!')
            self.gravando=True   

    def Botão_fotografar(self): 
        
        if not self.ligado:
            return print(f'{self.nome} Não Pode Fotografar Pois Não Esta Ligada!') 
        
        if self.gravando:
            return print(f'{self.nome} Não Pode Fotografar Pois, Está gravando!')

        print(f'{self.nome} Fotografou! ')
            

c1=Camera('Canon')
c2=Camera('Sony')

c1.Botão_ligar()
c1.Botão_fotografar()
print()

c1.Botão_gravar()
c1.Botão_fotografar()

c1.Botão_gravar()
print()

c1.Botão_ligar()
c1.Botão_fotografar()
c1.Botão_gravar()
print()

c1.Botão_ligar()
c1.Botão_fotografar()
c1.Botão_gravar()
print()



