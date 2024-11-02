#Sortear a ordem da apresentação de 4 alunos


import random
a1 = str(input('Digite um nome: '))
a2 = str(input('Digite outro nome: '))
a3 = str(input('Digite outro nome: '))
a4 = str(input('Digite outro nome: '))
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print('A ordem sorteada é')
print(alunos)