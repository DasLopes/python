'''Faça uma progressão aritmética e encerre o programa quando digitar 0'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + 10 * razão

cont = 0
while cont != décimo:
    print(cont, ' => ', end='')
    cont += 1    
print('ACABOU!')

termo = -1
while termo != 0:
    termo = int(input('Quantos termos quer mostrar? '))
    soma = cont + termo
    while cont != soma:
        print(cont, ' => ', end='')
        cont += 1    
    print('ACABOU!')
