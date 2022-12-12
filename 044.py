#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista dinheiro / cheque: 10% de desconto / À vista no cartão: 5% de desconto / em até 2x no cartão: Preço normal
#3x ou mais no cartão: 20% de juros

boneca = 150.00
carrinho = 123.99
videoGame = 2599.90
tablet = 1256.90
valor = 0

produto = str(input('Qual produto o senhor(a) vai levar? boneca, carrinho, video Game ou tablet' ))
pagamento = str(input('Qual forma de pagamento o senhor(a) vai utlilzar e será a vista ou parcelado? '))
if produto == boneca and