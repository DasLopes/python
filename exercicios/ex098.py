from time import sleep
def contador(i, f, p):
    if p < 0:
        p = p * -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
        print('FIM!')
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM!')

contador(10,0,-2)