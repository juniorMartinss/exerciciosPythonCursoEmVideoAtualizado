#Refaça o desafio 035 dos triâgulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais / - Isósceles: dois lados iguais / - Escaleno: todos os lados diferentes

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segunto segmanto: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR  triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

if r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3:
    print('O triângulo é isósceles, pois ele possui 2 lados iguais ({}, {}, {}).'.format(r1, r2, r3))
elif r1 == r2 and r3 or r2 == r1 and r3:
    print('O triâgulo é equilátero, pois ele possui os 3 lados iguais ({}, {}, {}).'.format(r1, r2, r3))