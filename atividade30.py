produtos = {
    1324: 6.45,
    6548: 2.37,
    987: 5.32,
    7623: 6.45,
    1001: 5.32
}

codigo = int(input("Digite o codigo do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

preco_unitario = produtos[codigo]
preco_total = preco_unitario * quantidade
print(f"Preço total: R$ {preco_total:.2f}")

