'''Mostre os 10 primeiros termos da progressão aritimetica usando a estrutura while'''

primeiro = 1#int(input('Primeiro termo: '))
razão = 1#int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
'''print('décimo: {}'.format(décimo))
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='=> ')
print('ACABOU')'''

cont = 1
while cont != décimo + 1:
    print(cont, ' => ', end='')
    cont += 1
print('ACABOU!')