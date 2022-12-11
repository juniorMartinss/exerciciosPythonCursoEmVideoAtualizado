#Crie um programa que leia um número REAL e mostre na tela a sua porção INTEIRA - EX: 6.127 -> 6

print('*' * 50)

import math
n = float(input('Digite um número com ponto: '))
r = math.floor(n)
print('O número digitado foi {} e a porção inteira é {}'.format(n, r))

print('*' * 51)

'''#formas que o prof. realizou

from math import trunc

num = float(input ('Digite um número com ponto: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#outra maneira

num = float(input('Digite um valor com ponto: '))
print('O valor digitado foi {} e a sua porção interia é {}'.format(num, int(num)))'''



