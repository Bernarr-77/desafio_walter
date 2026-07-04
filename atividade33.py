texto = input("Digite o texto: ")
palavras_invalidas = ["futebol", "religião", "política"]

if any(palavra in texto for palavra in palavras_invalidas):
    print("Texto invalido")
else:
    caracteres = len(texto.replace(" ", ""))
    print(f"O texto: \n{texto}\nTem {caracteres} caracteres")