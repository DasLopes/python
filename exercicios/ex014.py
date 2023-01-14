'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

temp = float(input('Informe a temperatura em ºC: '))
novo = temp * 1.8 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(temp, novo))
