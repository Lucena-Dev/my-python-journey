produto = float(input('Digite o valor do produto: R$'))

desconto = produto * 10 / 100
valor_final = produto - desconto

print(f'O produto com 10% de desconto fica R${valor_final}')
