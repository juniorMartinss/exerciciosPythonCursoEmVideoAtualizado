#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h.
# Mostrar uma mesangem dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada KM acima dos limite.

v = float(input('Digite a velocidade do veículo: '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi MULTADO por está na velocidade {}, e você terá que pagar R${:.2f}'.format(v, m))
else:
    print('Sua velocidade é {}, PARABÉNS! Você está dentro do limite de velocidade.'.format(v))
