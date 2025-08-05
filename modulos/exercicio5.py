import math

numero = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

potencia = math.pow(numero, numero2)
arredondado_cima = math.ceil(potencia)
arredondado_baixo = math.floor(potencia)

print(f"\n{numero} elevado a {numero2} é {potencia}")
print(f"Arredondado para cima: {arredondado_cima}")
print(f"Arredondado para baixo: {arredondado_baixo}")
