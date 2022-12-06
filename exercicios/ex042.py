ladoA = int(input('Lado A: '))
ladoB = int(input('Lado B: '))
ladoC = int(input('Lado C: '))

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    triangulo = 'sim'
    if ladoA == ladoB and ladoA == ladoC and ladoB == ladoC:
        tipo = 'Equilátero'
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
else:
    triangulo = 'não'

if triangulo == 'sim':
    print('Formou trinâgulo: {}, do tipo: {}.'.format(triangulo, tipo))
else:
    print('Formou triângulo? {}'.format(triangulo))