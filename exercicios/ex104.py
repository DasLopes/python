def leiaInt(msg):   
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)          
            break
        else:
            print('ERRO! Digite um número inteiro válido.')       
    return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')