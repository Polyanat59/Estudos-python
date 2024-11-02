nun1 = int(input('Digite um numero:'))
nun2 = int(input('Digite outro numero'))
nun3 = int(input('Digite outro'))

if nun1 < nun2 < nun3:
    print(f'{nun1} é maior')

elif nun2 < nun1 < nun3:
    print(f'{nun2} é maior')

else:
    print(f'{nun3} é maior')