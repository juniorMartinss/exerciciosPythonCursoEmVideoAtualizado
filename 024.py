#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

nome = str(input('Digite o nome de uma cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')

