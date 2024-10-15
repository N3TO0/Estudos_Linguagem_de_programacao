#Codigo com objeto, sendo importada para esse arquivo
import json
from Ex_07_a import caminho_arquivo, Pessoa

with open(caminho_arquivo,'r') as arquivo:

    dados = json.load(arquivo)

    for linha in dados:
        
        for chave, valor, in linha.items():
            print('\n',chave,':', valor)
        print("#-------------------------") 
        