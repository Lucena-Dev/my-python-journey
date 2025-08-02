import random

numero = int(input('Tente adivinhar o número em que estou pensando. \nDICA: É um número inteiro entre 1 a 10: '))

s = random.randint(1, 10)

print(f'Número que você escolheu: {numero}')
print(f'Número eu pensei: {s}')
