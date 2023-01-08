def leiaInt(n):
    n = str(input('Digite um número: '))
    if n.isnumeric():
        return n
    else:
        
        return 'ERRO! Digite um número válido.'


leiaInt()

'''
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''