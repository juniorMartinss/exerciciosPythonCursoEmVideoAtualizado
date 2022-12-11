#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "a"
#Em que posição ela aparece a primeira vez
#em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
print('A frase {}, tem {} veze(s) a letra "A".'.format(frase, frase.upper().count('A')))
print('A letra "A" na frase {}, aparece a primeira vez na posição {}.'.format(frase, frase.upper().find('A')+1))
print('A ultima vez que aparece a letra "A" na {} é na posição {}.'.format(frase, frase.upper().rfind('A')+1))