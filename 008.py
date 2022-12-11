#Escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milímetro

vm = float(input('Digite um valor em metros: '))
cm = vm * 100
mm = vm * 1000

print('O valor digitado em metros: {}, corresponde em cm: {} e em mm: {}'.format(vm, cm, mm))