"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
calcule e mostre o comprimento da hipotenusa."""


"""import math

oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))
hipo = oposto**2 + adjacente**2
print(f'O comprimento da hipotenusa é {math.sqrt(hipo):.2f}')
ABAIXO OUTRA FORMA DE RESOLVER"""


from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipo:.2f}')