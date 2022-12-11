#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nomeseparadamente.
#ex: Ana Maria De Souza - Primeiro: Ana - Último: Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer! Seu primeiro nome é {}, e seu último nome é {}.'.format(nome[0], nome[len(nome)-1]))