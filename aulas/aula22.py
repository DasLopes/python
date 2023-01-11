'''
modularização: ato de construir modulos

* Surgiu no início da década de 60
* Sistemas ficando cada vez maiores
* Foco: dividir um programa grande
* Foco: aumentar a legibilidade
* Foco: facilitar a manutenção
'''
# = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA 
def pratica():
    print(' = AULA PRÁTICA = ' * 10)
pratica()

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')