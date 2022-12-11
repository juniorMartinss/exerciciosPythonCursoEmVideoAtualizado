#Escreva um programa que converta uma temperatura digitada em °c converta para °F

c = float(input('Qual á temperatura hoje em °C? '))
f = c * 1.8 + 32
print('A temperatura de {}°C é equivalente a {}°F'.format(c,f))

#formula realizada pelo professor

fh = 9 * c / 5 + 32
print(fh)
