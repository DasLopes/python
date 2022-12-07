peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

print('Seu imc: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 26:
    print('Peso ideal')
elif imc < 31:
    print('Sobrepeso')
elif imc < 41:
    print('Obesidade')
else:
    print('Obesidade mórbida')