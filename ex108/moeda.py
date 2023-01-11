def metade(preço = 0):
    return preço / 2

def dobro(preço = 0):
    return preço * 2

def aumentar(preço = 0, taxa = 0):
    return preço + (preço / 100 * taxa)

def diminuir(preço = 0, taxa = 0):
    return preço - (preço / 100 * taxa)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')