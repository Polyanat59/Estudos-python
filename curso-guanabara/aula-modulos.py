import math
nun: int = int(input('digite um número: '))
raiz = math.sqrt(nun)
print(f'A raiz de{nun} é igual a {raiz:.2f}')

  # outra forma

from math import sqrt

numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print(f'A raiz de {numero} é igual a {raiz:.2f}')
