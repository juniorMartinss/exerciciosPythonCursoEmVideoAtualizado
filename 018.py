#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

print('*' * 51)

from math import radians, sin, cos, tan

ang = float(input('Digite o valor do ângulo: '))

rad = radians(ang)

sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print('O seno do ângulo {} é {:.4f}, o cosseno é {:.4f} e a tangente é {:.4f}'.format(ang, sen, cos, tan))

print('*' * 51)

