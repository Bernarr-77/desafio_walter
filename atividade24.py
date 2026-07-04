lista = ['João', 56, 'Gilberto', 46, 'Antonio', 35, 'Enzo', 12]


nomes = lista[::2]  
idades = lista[1::2]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos de vida")
    