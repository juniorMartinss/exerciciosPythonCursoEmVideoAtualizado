#Crie um programa que leia um número inteiro e mostre na tela se  ele é PAR ou ÍMPAR.

n = int(input('Digite um número inteiro: '))
r = n / 2

if r % 1:
    print('O número {}, é ÍMPAR'.format(n))
else:
    print('O número {}, é PAR'.format(n))