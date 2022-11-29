'''
Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente
de um triangulo retangulo, calcule e
mostre o comprimento da hipotenusa.
sqrt(x*x + y*y)
'''
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

'''
from math import sqrt
x = float(input('cateto oposto: '))
y = float(input('cateto adjacente: '))
hip = sqrt(x*x + y*y)
print('hipotenusa: {}'.format(hip))
'''