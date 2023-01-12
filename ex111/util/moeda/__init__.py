def metade(preço = 0, formato = False):
    """
        Calcula o aumento de um determinado produto
    retornando o resultado com ou sem formatação.
    :param preço: preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer a saída formatada ou não?
    :retrun: o valor reajustado, com ou sem formato.
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

def resumo(preço = 0, taxaa = 10, taxar = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)