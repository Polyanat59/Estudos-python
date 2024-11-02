nome = input("Digite seu nome completo: ").strip()
#strip para remove espaços inuteis
print(f"Seu nome com todas as letras em maisculo é {nome.upper()}")
print(f"Seu nome com todas as letras minusculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
#conta quantas lentras subtraindo os espaços

#print(f"Seu primeiro nome tem {nome.find(" ")} letras")
separa = nome.split()
print(f"Seu primriro nome é {separa[0]} e ele tem {len(separa[0])} letras")