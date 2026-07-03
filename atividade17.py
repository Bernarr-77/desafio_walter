notas = []
while True:
    print("Digite (fim) para calcular a media")
    user = input("Digite a nota: ")
    if user == "fim":
        media = sum(notas) / len(notas)
        print(media)
        break
    user = float(user)
    notas.append(user)
    continue
    