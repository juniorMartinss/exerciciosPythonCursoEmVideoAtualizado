#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.
print('*' * 51)

from random import choice

nome = input('Digite o nome do primeiro aluno(a): ')
nome2 = input('Digite o nome do segundo aluno(a): ')
nome3 = input('Digite o nome do terceiro aluno(a): ')
nome4 = input('Digite o nome do quarto aluno(a): ')

lista = [nome, nome2, nome3, nome4]
sorteio = choice(lista)

print('Os particpantes da disputa para apagar o quadro são {}, {}, {}, {} e o sorteado(a) é:\n{}, Parabéns!!! Você vai apagar o quadro. '.format(nome, nome2, nome3, nome4, sorteio))

print('*' * 51)

