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

def resumo(preço, aumento, desconto):
    print('-' * 30)
    print('       RESUMO DO VALOR      ')
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'Dobro do preço: {dobro(preço, True)}')
    print(f'Metade do preço: {metade(preço, True)}')
    print(f'{aumento}% de aumento: {aumentar(preço, aumento, True)}')
    print(f'{desconto}% de redução: {diminuir(preço, desconto, True)}')
    print('-' * 30)
