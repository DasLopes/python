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