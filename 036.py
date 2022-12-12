#escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
#não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual valor do imóvel que o senhor(a) deseja comprar? '))
salario = float(input('Qual o salário do senhor(a)? '))
qntPrest = int(input('Quantas parcelas o senhor(a) deseja parcelar? '))

valMax = salario * 1.30 - salario
valParc = casa / qntPrest

if valParc > valMax:
    print('Seu empréstimo bancário foi NEGADO! O Valor da parcela ficou ACIMA de 30% do seu salário! O valor final da parcela ficou R$ {:.2f} e o máximo seria R$ {:.2f}.'.format(valParc, valMax))
else:
    print('Seu empréstimo foi APROVADO! Parabéns! O valor da sua parcela será de R$ {:.2f}.'.format(valParc))