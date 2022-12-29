# faça um progrma que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar. / Se é a  hora de se alistar. / Se  já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento (ex: 1986): '))

idade = atual - nasc


if idade < 18:
    falta = 18 - idade
    print('Você ainda vai ser alistar no serviço militar, pela sua idade ({}), falta {} ano(s).'.format(idade, falta))
elif idade == 18:
    print('Você está no período de alistamento. Devido a sua idade ({}) você deve se alistar IMEDIATAMENTE!'.format(idade))
else:
    passou = idade - 18
    print('Você passou o período de alistamento. Devido a sua idade ({}), você esta atrasado em {} anos(), regularize-se!'.format(idade, passou))

