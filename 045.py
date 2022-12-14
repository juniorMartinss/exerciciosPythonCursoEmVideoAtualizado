#Crie um programa que faça o computador jogar jokenpô com você

import random
from time import sleep

print('-='*15, 'JOKENPÔ', '-='*15)

jogador = str(input('pedra, papel ou tesoura? '))
print('-='*15, 'computador', '-='*15)
print('processando...')
sleep(1.5)

lista = ['pedra', 'papel', 'tesoura']
computador = (random.choice(lista))
print(computador)
print('-='*30)

if jogador == 'tesoura' and computador == 'tesoura':
    print('EMPATE,! Ninguém venceu essa!')
elif jogador == 'tesoura' and computador == 'papel':
    print('PARABÉNS, você VENCEU!')
elif jogador == 'tesoura' and computador == 'pedra':
    print('PERDEU! Computador GANHOU!')
elif jogador == 'papel' and computador == 'tesoura':
    print('PERDEU! Computador GANHOU!')
elif jogador == 'papel' and computador == 'papel':
    print('EMPATE,! Ninguém venceu essa!')
elif jogador == 'papel' and computador == 'pedra':
    print('PARABÉNS, você VENCEU!')
elif jogador == 'pedra' and computador == 'tesoura':
    print('PARABÉNS, você VENCEU!')
elif jogador == 'pedra' and computador == 'papel':
    print('PERDEU! Computador GANHOU!')
elif jogador == 'pedra' and computador == 'pedra':
    print('EMPATE,! Ninguém venceu essa!')

print('-='*15, 'GAME OVER', '-='*15)
