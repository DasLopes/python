'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

menu = 4
while menu != 5:
    if menu == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))    

    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')

    menu = int(input('Escolha sua uma opção: '))  
    
    if menu == 1:            
        soma = n1 + n2
        print('Resultado da soma: {}'.format(soma))
    if menu == 2:
        mult = n1 * n2
        print('Resultado da multiplicação: {}'.format(mult))
    if menu == 3:
        if n1 > n2:
            print('O primeiro número é o maior')
        else:
            print('O segundo número é o maior.')
    