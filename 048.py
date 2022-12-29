# Faça um programa  que calcule a soma entre todos os números ímpares que  são multiplos de 3 e que se encontram no
#intervalo de 1 até 500.

cont = 0
soma = 0

for c in range(1, 500+1):
    if c % 2 == 1 and c % 3 == 0:
        cont += 1
        soma += c
print('A quantidade de números multiplos de 3 no intervalo de 1 até 500 é: {}, e a soma deles é: {}'.format(cont, soma))


