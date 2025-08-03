nome = str(input('Digite o seu nome: ')).strip()

espaco = nome.replace(" ", "")
letras = len(espaco)
maiuscula = nome.upper()
minuscula = nome.lower()

print(f'Ao total, seu nome tem {letras} letras')
print(f'Seu nome em letras maiúsculas: {maiuscula}')
print(f'Seu nome em letras minúsculas: {minuscula}')
