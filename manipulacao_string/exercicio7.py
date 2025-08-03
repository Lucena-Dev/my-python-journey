nome = str(input('Qual o seu nome? ')).strip().upper()

dividir = nome.split()
primerio_nome = dividir[0]

print('O seu nome começa com Ana? {}'.format('ANA' in primerio_nome))
