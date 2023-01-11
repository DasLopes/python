def metade(preço):
    return preço / 2

def dobro(preço):
    return preço * 2

def aumentar(preço, taxa=0):
    return preço + (preço / 100 * taxa)

def diminuir(preço, taxa=0):
    return preço - (preço / 100 * taxa)