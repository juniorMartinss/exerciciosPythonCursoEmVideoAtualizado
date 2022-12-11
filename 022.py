#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúculas.
#O nome com todas as letres minúsculas.
#Quantas letras ao todos (sem considerar espaços)
#Quantas letras tem o primeiro nome.


nc = str(input('Digite o nome completo: ')).strip()

print('O nome em letra maiúscula é: {}'.format(nc.upper()))
print('O nome em letra minúscula é: {}'.format(nc.lower()))
print('A quantiade de caracteres no nome é: {} letras'.format(len(nc) - nc.count(' ')))
divi = nc.split()
print('A quantidade de caracteres no primeiro nome é: {}'.format(len(divi[0])))
print('Seu nome primeiro nome tem {} letras '.format(nc.find(' ')))

