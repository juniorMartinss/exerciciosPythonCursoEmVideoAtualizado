#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria.
#de acordo com a idade: - Até 9 anos: Mirim / - Até 14 anos: Infantil / - Até 19 anos: Junior / - Até 20 anos: Sênior / Acima: Master

nasc = int(input('Digite o ano do seu nascimento (ex:1986): '))

idade = 2022 - nasc

if idade <= 9:
    print('CATEGORIA: Mirim - Idade: {}'.format(idade))
elif idade > 9 and idade < 15:
    print('CATEGORIA: Infantil - Idade: {}'.format(idade))
elif idade > 14 and idade < 20:
    print('CATEGORIA: Junior - Idade: {}'.format(idade))
elif idade > 19 and idade < 21:
    print('CATEGORIA: Senior - Idade: {}'.format(idade))
else:
    print('CATEGORIA: Master - Idade: {}'.format(idade))

