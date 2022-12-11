#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de  tinta
# necessário para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2m quadrados

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
pint = area / 2

print('A area da parede corresponde a: {}, e é necessário {} litros para pintar toda a parede.'.format(area, pint))
