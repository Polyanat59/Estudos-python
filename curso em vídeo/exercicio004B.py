# O mesmo exercicio 004, porém, agora com a sintaxe nova
n = input('Digite algo: ')
print(f'O tipo deste valor é: {type(n)}')
print(f'É somente espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumerico? {n.isalnum()}')
print(f'Esta tudo maiúsculo? {n.isupper()}')
print(f'Esta tudo minúsculo? {n.islower()}')
print(f'esta capitalizado? {n.istitle()}')