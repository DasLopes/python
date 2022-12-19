fatorial = int(input('Digite um número: '))
print('Fatorial: ', fatorial, ' ', end='')
cont = fatorial
for c in range(1, fatorial):
    fatorial = fatorial * (cont - 1)
    cont -= 1
    print(cont, ' ', end='')
print('= ', fatorial)