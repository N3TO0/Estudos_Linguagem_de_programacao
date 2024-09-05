#CODIGO PARA SIMULAR ANALISE DE EMPRESTIMO.
from time import sleep
print("\n{:=^150}".format("Emprestimo"))

c=float(input("\nQual o valor da Casa ? : ").strip()) 
s=float(input("\nQual o valor total do seu salario ? : ").strip()) 
a=float(input("\nDeseja quitar a casa em quantos anos ? : ").strip()) 
b=(a*12) #Quantidade de meses no total 
e=c/b #Valor das parcelas  
f=(s*30)/100 #  30% do valor do salario 

if e > f:
    print("\nCalculando..")
    sleep(2)
    print("\nSinto muito, mas de acordo com a analise\n Esse emprestimo não é possivel!")
else:
    print("\nParabens!! Seu emprestimo foi aprovado!!\nO valor das parcelas serão de: R$ {:.2f}".format(e))


print("\n\n{:=^150}".format("Fim"))

