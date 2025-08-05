numero = float(input('Quantos Km é a sua viagem? '))

if numero <=200:
    print('O preço da sua passagem é R$0.50 por Km.')
    print('O preço total ficou R${}'.format(numero * 0.50))
else:
    print('O preço da sua viagem é R$0,45 por km.')
    print('O preço total ficou R${}'.format(numero * 0.45))
