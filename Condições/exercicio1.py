import random

numero = int(input('Tente adivinhar o número: '))
numero2 = random.randint(0, 5)

if numero == numero2:
    print('Parabens, você acertou!')
else:
    print('Você errou,tente novamente.')
print(f'O número pensado foi {numero2}')
