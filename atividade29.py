possiveis_convidados = ["Bernardo", "Marcos", "Melissa", "Vitor"]
banidos = ["Vitor", "Marcos"]
convidados = [nomes for nomes in possiveis_convidados if nomes not in banidos]
print(convidados)