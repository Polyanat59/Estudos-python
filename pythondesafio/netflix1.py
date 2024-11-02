import pandas as pd

tabela = pd.read_csv("netflix_titles.csv")

#Utilizei 'values' para retornar os valores das colunas
colunas = tabela.columns.values
print(f"\nColunas da tabela: \n {colunas}\n\n")
print("-"*70)


#Criei uma lista vazia para armazenar a coluna type, com movie separado
lista_de_filmes = []
#Interou sopre as linhas da planilha
for indice, linha in tabela.iterrows():

    #Condicional para mover movie para a lista vazia
    if linha["type"] == "Movie":
        lista_de_filmes.append(linha["type"])

        #para retornar o número de objetos
        quantidade_de_filmes = len(lista_de_filmes)

print(f"A quantidade de filmes disponiveis é: {quantidade_de_filmes}\n\n")
print("-"*70)

#Contando quantas vezes o diretor aparece na tabela
contagem_dire = tabela["director"].value_counts()
print(contagem_dire)

#retorna os 5 primeiros
diretores_com_mais_filmes = contagem_dire.head(5)
print(f"\nOs 5 diretores com mais filmes: {diretores_com_mais_filmes}\n\n")
print("-"*70)

#relacionei as duas colunas atraves do crosstab.  adicionei os totais 'margins=True' e margins_name=
diretores_atores = pd.crosstab(index=tabela['director'], columns=tabela['cast'], margins=True, margins_name='total')
print(f"Diretores que atuaram como atores em suas produções: {diretores_atores}\n\n")
print("-"*70)


#Busquei todos os anos que tem na tabela
ano = tabela["release_year"].value_counts()
print(ano)
# busca o 1° maior
ano_mais_lancamentos = ano.head(1)
print(f"O ano que teve o maior número de lançamentos: {ano_mais_lancamentos}")
