#O mesmo professor do desafio anterior(019) quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle#importei para usar o metodo que o prf° utilizou

'''maneira que eu fiz não fez o a sequecia aleatoria
nome1 = input('Digite o nome do 1° aluno(a): ')
nome2 = input('Digite o nome do 2° aluno(a): ')
nome3 = input('Digite o nome do 3° aluno(a): ')
nome4 = input('Digite o nome do 4° aluno(a): ')

lista = [nome1, nome2, nome3, nome4]
seqApres = sorted(lista)

print('Os partcipantes para apresentação dos trabalhos são: {}, {}, {}, {}.\nA sequência de apresentação é {}'.format(nome1, nome2, nome3, nome4, lista))'''

print('*' * 51)

#maneira que o professor fez

n1 = input('Digite o nome do 1° aluno(a): ')
n2 = input('Digite o nome do 2° aluno(a): ')
n3 = input('Digite o nome do 3° aluno(a): ')
n4 = input('Digite o nome do 4° aluno(a): ')

lis = [n1, n2, n3, n4]
shuffle(lis)

print('A sequêcia de apresentação é: {}(Maneira que o professor fez)'.format(lis))

print('*' * 51)
