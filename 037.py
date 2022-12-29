#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 - para binário / 2 - octal / 3 - hexadecimal

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das opções: 
[ 1 ] Converter Binário.
[ 2 ] Converter para Octal.
[ 3 ] Converter Hexadecimal. ''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é igual: {}.'.format(opcao, bin(num)))
elif opcao == 2:
    print('{} convertido para octal é igual: {}.'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual: {}.'.format(opcao, hex(num)))
else:
    print('Digite uma opção VÁLIDA!!!')