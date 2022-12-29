#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
#tabela abaixo: - Abaixo de 18.5: Abaixo do peso / Entre 18.5 e 25: Peso ideal / 25 até 30: Sobrepeso / - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (alt * alt)

if imc < 18.5:
    print('Você está ABAIXO DO PESO! Seu IMC está {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL! Seu IMC está {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO! Seu IMC está {:.1f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE! Seu IMC está {:.1f}'.format(imc))
else:
    print('Você está com OBESIDADE MÓRBIDA! Seu IMC está {:.1f}'.format(imc))
