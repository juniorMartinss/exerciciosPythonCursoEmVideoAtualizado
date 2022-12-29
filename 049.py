#refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

n = int(input('Digite um número que deseja visualizar a tabuada: '))

for c in range(0, 11):
    tabuada = c * n
    print('Segue a tabuada: {} x {} = {}'.format(n, c, tabuada))