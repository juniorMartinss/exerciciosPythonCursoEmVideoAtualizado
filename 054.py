#Crie um programa que leia o ano do nascimento de sete pessoas. no final. Mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores. (considerar 21 anos)

from datetime import date#Importando da biblioteca datetime, data do calendario atual

hoje  = date.today().year#instaciando a variavel hoje com a data atual do dia
contM = 0
cont  = 0

#criando o laço de repetição FOR
for c in range(1, 8):
    nasc = int(input('Digite o {}° ano de nascimento: '.format(c)))#Pedindo os dados para o usuário
    maior = hoje - nasc
    if maior >= 21:
        contM += 1
    else:
        cont += 1
print('Das 7 datas de nascimento digitadas, são maiores de idade: {}, e menores de idade: {}'.format(contM, cont))
