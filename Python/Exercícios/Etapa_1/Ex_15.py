a=float(input("\nDigite o preço do produto:"))
b=float(input("\nDigite quantos porcento ganhou de desconto:"))
c=((a*b)/100)

print("O desconto é de {:.2f} R$\nValor total com desconto é: {:.2f} R$".format(c,a-c))