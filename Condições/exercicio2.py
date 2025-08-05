km = float(input('Qual a velocidade que o seu carro estar? km/h '))
multa = (km - 80) * 7

if km > 80:
    print('Você foi multado.')
    print(f'O valor da multa é de {multa}R$')
else:
    print('Você não foi multado.')
