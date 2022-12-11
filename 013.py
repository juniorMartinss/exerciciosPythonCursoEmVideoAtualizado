#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input('Digite o salário do colaborador(a): R$'))
nsal = sal * 0.15 + sal

print('O antigo do salário do colaborador(a) era R$ {:.2f}, agora após o aumento de 15%, passa a ser: R$ {:.2f}'.format(sal, nsal))

