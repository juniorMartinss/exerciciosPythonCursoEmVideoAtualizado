#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem. Cobrando R$0.50 por
# Km para viagens até 200Km e R$ 0.45 para viagens mais longas.

Km = float(input('Qual a distância da sua viagem em Kilometros: '))

if Km <= 200:
    v = Km * 0.50
    print('O valor da sua viagem de {} kilometros é R$ {:.2f}.'.format(Km, v))
else:
    v = Km * 0.45
    print('O valor da sua viagem de {} kilometros é R$ {:.2f}.'.format(Km, v))
