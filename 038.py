#Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
#O primeiro valore é maior / O segundo valor é maior / Não existe valor maior, os dois são iguais

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))

if n1 > n2:
    print('O primeiro valor ({}) é maior do que o segundo valor({}).'.format(n1, n2))
elif n1 < n2:
    print('O segundo valor ({}) é maior que o primeiro valor ({}) digitado.'.format(n2, n1))
else:
    print('Não existe valor maior, os dois valores digitados ({}, {}), são iguais.'.format(n1, n2))

