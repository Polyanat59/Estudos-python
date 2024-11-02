#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e antecessor

n1 = int(input('Digite um número: '))
sucessor = (n1 + 1)
antecessor = (n1 - 1)
print(f'O antecessor de {n1} é {antecessor} e o sucessor é {sucessor}')




#outra forma caso não precise guardar a variavel

n = int(input('Digite um número: '))
print(f'Analisando o valor {n}, seu antecessor é {n-1} e o sucessor é {n+1}')