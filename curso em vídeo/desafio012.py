# Faça um algoritimo que leia o preço de um produto e motre seu novo preço com 5% de desconto.

preço = float(input('Digite o preço do produto: R$ '))
desconto = preço * 5 / 100
total = preço - desconto
print(f'O valor do produto com o desconto de 5% é R${total :.2f}')
