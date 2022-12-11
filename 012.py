#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

val = float(input('Digite o valor do produto: R$'))
nval = val * 0.05
desc = val - nval
print('O novo valor do produto que era {}, acresentando 5% é: {:.2f}'.format(val, desc))

#forma realizada pelo professor (conta de porcetagem)

desc1 = val - (val * 5 / 100)
print('R$',desc1)