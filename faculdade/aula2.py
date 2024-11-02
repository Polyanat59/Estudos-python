#verifique se é ímpar ou par
nun = int(input('Digite um número: '))
resto = nun % 2

if resto == 0 :
    print(f'{nun}  é par')
else:
    print(f'{nun} é ímpar')