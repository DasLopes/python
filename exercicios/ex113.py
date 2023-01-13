def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n



n1 = leiaInt('Digite um número inteiro: ')
#n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro foi {n1} e o real foi {n1}')