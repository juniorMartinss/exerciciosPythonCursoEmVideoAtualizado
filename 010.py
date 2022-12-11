#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (considere  US$ 1,00 = 5,26 (cotação 10/07/2022)

din = float(input('Qual valor você tem na sua carteira? R$'))
dol = din / 5.26
print('O valor que você pode comprar em dólares são: Us${:.2f}'.format(dol))