'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

d = float(input('Uma distência em metros: '))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print('A medida de {}m corresponde a:'.format(d))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))

