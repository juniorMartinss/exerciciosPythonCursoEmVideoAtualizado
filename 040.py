#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado / - Média entre 5.0 e 6.9: Recuperação / - Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a 1° nota do aluno(a): '))
nota2 = float(input('Digite a 2° nota do aluno(a): '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('O aluno(a) está REPROVADO! Sua média foi {:.2f}.'.format(media))
elif media >= 5 and media < 7:
    print('O aluno(a) está em RECUPERAÇÃO! Sua média foi {:.2f}.'.format(media))
else:
    print('O aluno está APROVADO! Sua média foi {:.2f}.'.format(media))