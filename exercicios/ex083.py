'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expr = '((a+b)*c)(x+y(3+2/3)*z)'#'((((a+b)*c)+2)/4))' #str(input('Digite a expressão: '))
a = b = 0
for c in expr:    
    if '(' == c:
        a += 1
    if ')' == c:
        b += 1
if a == b:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
