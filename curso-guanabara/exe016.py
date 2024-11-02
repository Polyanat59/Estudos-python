'''Crie um programa que leia um número real qualquer e mostre na  tela a sua porção inteira
from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a porção inteira é {trunc(num)}')'''

#outra forma

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')