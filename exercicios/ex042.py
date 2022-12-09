ladoA = int(input('Lado A: '))
ladoB = int(input('Lado B: '))
ladoC = int(input('Lado C: '))

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    print('Os segmentos acima PODEM FORMAR um triângulo do tipo: ', end='')
    if ladoA == ladoB == ladoC:
        tipo = 'Equilátero'
    elif ladoA != ladoB != ladoC != ladoA:
        tipo = 'Escaleno'
    else:
        tipo = 'Isósceles'
else:
    print('Não formou um triângulo.')