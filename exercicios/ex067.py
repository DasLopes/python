'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    else:
        print('-' * 40)
        for c in range(1, 11):
            p = c * num
            print(f'{num} x {c} = {p}')
        print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')