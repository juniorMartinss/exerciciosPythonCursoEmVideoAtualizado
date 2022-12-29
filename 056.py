#Desenvolvar um programa que leia  o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do
# grupo. / Qual é o nome do homem mais velho / Quantas mulheres tem menos de 20 anos.

#criando as variaveis globais
somaIdade  = 0
mediaIdade = 0
maiorIdade = 0
nomeVelho  = ''
totMulher  = 0

for i in range(1, 5):#inicio do contador
    print('-------- {}° PESSOA --------'.format(i))
    nome = str(input('Digite o nome da {}° pessoa: '.format(i))).strip()#para o usuario digitar e mostrar em tela
    idade = int(input('Digite a idade da {}° pessoa: '.format(i)))#para o usuario digitar e mostrar em tela
    sexo = str(input('Digite o sexo da {}° pessoa [F/M]: '.format(i))).strip()#para o usuario digitar e mostrar em tela
    somaIdade += idade#guardando na variavel somaIdade a soma de todas as idades para depois verificar a média
    if i == 1 and sexo in 'Mm':#guardando a referencia nas variaveis para analise do programa
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:#analisando so dados
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher += 1

mediaIdade = somaIdade / 4#verificando a média
print('A média de idade do grupo é: {} anos.'.format(mediaIdade))#resultado das analises e mostrando em tela
print('O nome do homem mais velho é: {}, e sua idade é: {} anos.'.format(nomeVelho, maiorIdade))
print('No grupo existem {} mulheres menores de 20 anos.'.format(totMulher))

