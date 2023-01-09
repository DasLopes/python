def leiaInt():
    n = str(input('Digite um número: '))
    if n.isnumeric():
        return n
    else:        
        return 'ERRO! Digite um número válido.'


#leiaInt()


leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')