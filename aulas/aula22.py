'''
modularização: ato de construir modulos

* Surgiu no início da década de 60
* Sistemas ficando cada vez maiores
* Foco: dividir um programa grande
* Foco: aumentar a legibilidade
* Foco: facilitar a manutenção
'''

'''
Vantagens

* Organização do código
* Facilidade na manutenção
* Ocultação de código detalhado
* Reutilizar em outros projetos
'''
# = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA PRÁTICA =  = AULA 
from uteis import numeros

numeros.pratica()

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')