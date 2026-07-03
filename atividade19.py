vidas = 7
palavra_secreta = "hello world"
progresso = ["_"] * len(palavra_secreta.replace(" ", ""))

while True:
    chute = input("Digite sua tentativa: ")
    acertou = False

    for i, letra in enumerate(palavra_secreta):
        if letra == chute:
            acertou = True
            progresso[i] = letra

    if not acertou:
        vidas -= 1

    print(f"{progresso}\nQuantidade de vidas: {vidas}")

    if chute == palavra_secreta:
        print("Você acertou!")
        break
    
