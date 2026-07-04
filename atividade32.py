valor_total = 1
valor_inicial = 1

for _ in range(2,65):
    valor_inicial = valor_inicial * 2
    valor_total += valor_inicial

print(valor_total)