largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
rendimento = 2
tinta = area / rendimento
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))
