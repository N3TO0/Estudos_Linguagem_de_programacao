#CODIGO DE UM JOGO DE ADIVINHAÇÃO.

import random
g="  Jogo da Sorte  "
f="  fim  "
n=random.randint(0,5)

print("\n\n{:=^50}".format(g))

b=int(input("\nTente adivinhar qual numero é de 0 a 5: ").strip())

if b==n:
 print("\nParabéns você acertou!! o numero era {}".format(n))
else:
 print("\nQue pena, você errou o numero era: {}".format(n))

print("\n{:=^50}".format(f))