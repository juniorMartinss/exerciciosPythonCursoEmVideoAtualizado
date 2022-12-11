#faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

v1 = float(input('Digite o 1° valor: '))
v2 = float(input('Digite 0 2° valor: '))
v3 = float(input('Digite o 3° valor: '))

#forma "comum" de realizar o exercicio do menor e maior número
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

maior = v1
if v2 > v1 and v2 > v3:
     maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print ('O menor número digitado foi: {}.'.format(menor))
print ('O maior número digitado foi: {}.'.format(maior))





