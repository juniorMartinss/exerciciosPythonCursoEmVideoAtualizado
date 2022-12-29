#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#ex: APOS A SOPA (DE TRAS PARA FRENTE É IGUAL)

frase = str(input('Digite uma frase: ')).strip().upper()#STRIP tira os espaços9inicio e fim da frase), UPPER deixa o que foi digita em maiusculo
palavras = frase.split()#SPLIT separando as palavras ex: biblia sagrada ('biblia' , 'sagrada')
junto = ''.join(palavras)#'' sem espaço + JOIN junta o que foi digitado remivendo todos os espaços
inverso = ''#estaciando uma variavel
for letra in range(len(junto) -1, -1, -1):#LEN é o tamanho no caso do que está na variavel JUNTO, -1 para mostrar a ultimo caractere, -1 para mostrar o primeiro caractere, -1 para começar de traz para frente
    inverso += junto[letra]#INVERSO recebe ele mesmo + a variavel JUNTO com o contator LETRA
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')


print('=' * 15, 'OUTRA MANEIRA DE FAZER O MESMO EXERCICIO', '=' * 15)

frase = str(input('Digite uma frase: ')).strip().upper()#STRIP tira os espaços9inicio e fim da frase), UPPER deixa o que foi digita em maiusculo
palavras = frase.split()#SPLIT separando as palavras ex: biblia sagrada ('biblia' , 'sagrada')
junto = ''.join(palavras)#'' sem espaço + JOIN junta o que foi digitado remivendo todos os espaços
inverso = junto[::-1]#fateamento do que foi digitado
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')