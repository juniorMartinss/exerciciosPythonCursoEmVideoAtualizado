#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista dinheiro / cheque: 10% de desconto / À vista no cartão: 5% de desconto / em até 2x no cartão: Preço normal
#3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS MARTINS '))

compras = float(input('Valor da compra: R$ '))

print('''Qual forma de pagamento: 
[0] Finalizar.
[1] À vista / Cheque.
[2] Débito.
[3] Crédito 2x .
[4] Crédito 3x ou mais.''')
opcao = int(input('Digite sua opção: '))

for != 0:
    if opcao == 1:
        valFinal = compras - (compras * 10 / 100)
        print('O valor da compra é R$ {:.2f}, com o desconto de pagamento à vista o preço final é R$ {:.2f}'.format(compras, valFinal))
    elif opcao == 2:
        valFinal = compras - (compras * 5 / 100)
        print('O valor da compra é R$ {:.2f}, com o desconto de pagamento no débito o valor final é R$ {:.2f}.'.format(compras, valFinal))
    elif opcao == 3:
        valParc = compras / 2
        print('Valor da final da compra é R$ {:.2f}, parcelado em 2x fica R$ {:.2f} por parcela.'.format(compras, valParc))
    else:
        parc = int(input('Quantas parcelas o Sr(a) deseja? '))
        valFinal = compras * 1.20
        valParc = valFinal / parc
        print('O valor da compra é R$ {:.2f}, devido o parcelamento em {}x, o valor final ficou R$ {:.2f}, com a parcela de R$ {:.2f}'.format(compras, parc, valFinal, valParc))