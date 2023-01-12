def metade(preço = 0, formato = False):
    """
    :param preço: recebe o preço de um produto
    :param taxa: recebe um valor em porcentagem
    :param formato: substitui o . por , e coloca 2 algarismos após a virgula.
    """
    res = preço / 2
    return res if formato is False else moeda(res)

def dobro(preço = 0, formato = False):
    """
    :param preço: recebe o preço de um produto
    :param taxa: recebe um valor em porcentagem
    :param formato: substitui o . por , e coloca 2 algarismos após a virgula.
    """
    res = preço * 2
    return res if formato is False else moeda(res)

def aumentar(preço = 0, taxa = 0, formato = False):
    """
    :param preço: recebe o preço de um produto
    :param taxa: recebe um valor em porcentagem
    :param formato: substitui o . por , e coloca 2 algarismos após a virgula.
    """
    res = preço + (preço / 100 * taxa)
    return res if formato is False else moeda(res)

def diminuir(preço = 0, taxa = 0, formato = False):
    """
    :param preço: recebe o preço de um produto
    :param taxa: recebe um valor em porcentagem
    :param formato: substitui o . por , e coloca 2 algarismos após a virgula.
    """
    res = preço - (preço / 100 * taxa)
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')