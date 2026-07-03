texto = input("Digite um texto")
vogais = "aeiou"
total_letras = len(texto.replace(" ", ""))
vogais_texto = [vogal for vogal in texto.lower() if vogal in vogais]
palavras = len(texto.split())
print(f" total de letras: {total_letras},\n Todas as vogais: {vogais_texto}\n Quantidade de palavras: {palavras}")

