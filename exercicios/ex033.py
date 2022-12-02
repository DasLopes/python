a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o maior
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
# Verificando quem é o menor
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
