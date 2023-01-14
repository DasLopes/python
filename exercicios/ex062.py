'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

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
