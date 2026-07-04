notas = [10,5,7,4,8]
frequencia = 70
media = sum(notas) / len(notas)
if media >= 6 and frequencia >= 70:
    print("Aprovado")
elif media >=6 and frequencia < 70:
    print("Reprovado por falta")
elif media <6 and frequencia < 70:
    print("Reprovado por falta e nota")