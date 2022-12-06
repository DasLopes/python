num = int(input('Digite um número inteiro: '))
print('( 1 ) para binário: ')
print('( 2 ) para octal: ')
print('( 3 ) para hexadecimal: ')
op = int(input('Digite uma das opções acima: '))
if op == 1:
    print('binário: {}'.format(bin(num)))
elif op == 2:
    print('Octal: {}'.format(oct(num)))
elif op == 3:
    print('Hexadecimal: {}'.format(hex(num)))
else:
    print('Opção inválida.')