# faça um progrma que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar. / Se é a  hora de se alistar. / Se  já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ouy que passou do prazo.
from datetime import date

nascimento = float(input('Qual a data do seu nascimento? '))
idade = date.today().year
print(idade)