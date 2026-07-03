import random

maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*"

tamanho = int(input("Digite o tamanho da senha: "))
usar_maiusculas = input("Quer incluir letras maiúsculas? (s/n): ").lower() == "s"
usar_minusculas = input("Quer incluir letras minúsculas? (s/n): ").lower() == "s"
usar_numeros = input("Quer incluir números? (s/n): ").lower() == "s"
usar_simbolos = input("Quer incluir símbolos? (s/n): ").lower() == "s"

opcoes = ""

if usar_maiusculas:
    opcoes += maiusculas
if usar_minusculas:
    opcoes += minusculas
if usar_numeros:
    opcoes += numeros
if usar_simbolos:
    opcoes += simbolos

senha = "".join(random.choice(opcoes) for _ in range(tamanho))
print(senha)