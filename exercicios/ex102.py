def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :parametro n: O número a ser calculado.
    :parametro show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            if c > 1:
                print(f'{c} x ', end='')
            else: 
                print(f'{c} = ', end='')
    return f
        

print(fatorial(5, True))