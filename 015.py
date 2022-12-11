# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kilometros o carro percorreu? '))
dias = int(input('Digite a quantidade dias que o carro permaneceu alugado: '))
pag = (dias * 60) + (0.15 * km)
print('O valor a ser pago considerando que o carro rodou {}km e ficou {} dias alugados é de R${:.2f}'.format(km, dias, pag))
