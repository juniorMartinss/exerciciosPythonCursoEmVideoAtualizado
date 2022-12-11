#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retâgulo. Calcule e
# mostre o comprimento da hipotenusa

print('#' * 50)

#exercicio usando a formula matemática da trigonometria(realizado por mim)
import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hip = (co**2)+(ca**2)
hip1 = math.sqrt(hip)

print('O valor do cateto oposto é {}, do cateto adjacente é {} e o valor da hipotenusa é {:.2f}'.format(co, ca, hip1))

print('#' * 51)

#Formula encontrada na internet

hipot = (co ** 2 + ca ** 2) ** (1/2)
print('O valor do cateto oposto é {}, do cateto adjacente é {} e o valor da hipotenusa é {:.2f}.(usando formula internet)'.format(co, ca, hipot))

print('#' * 51)

#formula realiza pelo prof°

hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))#formula realizada pelo professor




