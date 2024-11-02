"""Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado."""

dias = int(input('Você alugou o carro por quantos dias? '))
km = float(input('Quantos Km rodados? '))
k = km * 0.15
d = dias * 60
total = k + d
print(f"O valor por dias é {d}R$ e por Km é {k:.2f}R$, sendo assim o total é {total:.2f}R$")
