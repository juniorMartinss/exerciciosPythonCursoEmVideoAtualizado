#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final, mostre os 10
# primeiro termos dessa progressão.

primeiro = int(input('Primeiro termo: '))#solicitando dados para o usuário
razão = int(input('Razâo: '))#solicitando dados para o usuário
décimo = primeiro + (10 - 1) * razão#Calculo
for c in range(primeiro, décimo + razão, razão):#contador
    print('{} '.format(c), end='- ')#mostra em tela / Dentro do contador
print('Acabou.')#mostra em tela