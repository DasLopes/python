'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

ladoA = int(input('Lado A: '))
ladoB = int(input('Lado B: '))
ladoC = int(input('Lado C: '))

if ladoA < (ladoB + ladoC) or ladoB < (ladoA + ladoC) or ladoC < (ladoA + ladoB):
    print('Os segmentos acima PODEM FORMAR um triângulo do tipo: ', end='')
    if ladoA == ladoB == ladoC:
        print('Equilátero')
    elif ladoA != ladoB != ladoC != ladoA:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não formou um triângulo.')