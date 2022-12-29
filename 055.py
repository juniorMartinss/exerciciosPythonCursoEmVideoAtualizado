#faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#criando variaveis (não é necessário)
maior = 0
menor = 0

for p in range(1, 6):#contador
    peso = float(input('Digite o {}° peso: kg '.format(p)))#usuário digitar e mosra em tela
    if p == 1:#criando com if a referencia para analise dos dados
        maior = peso#guardando os valores de referencia nas variaveis
        menor = peso#guardando os valores de referencia nas variaveis
    else:#começando a analise de dados
        if peso > maior:#analisando os dados para o maior peso
            maior = peso
        if peso < menor:#analisando os dados para o menor peso
            menor = peso
print('O maior peso é: {}kg'.format(maior))#mostrando em tela os resultados
print('O menor peso é: {}kg'.format(menor))#mostrando em tela os resultados

