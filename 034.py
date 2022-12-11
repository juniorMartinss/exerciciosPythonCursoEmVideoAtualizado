#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
#superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite o salário do colaborador(a): R$ '))

if s > 1250:
    a = s * 1.10
    print('Devido seu salário ser R$ {},o seu aumento será de 10%, o seu novo salário é R$ {:.2f}!'.format(s, a))
else:
    a = s * 1.15
    print('Devido seu salário ser R$ {},o seu aumento será de 15%, o seu novo salário é R$ {:.2f}!'.format(s, a))