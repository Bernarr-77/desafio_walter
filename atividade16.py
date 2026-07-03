massa = float(input("Digite a massa: "))
altura = float(input("Digite a altura: "))
raio = float(input("Digite o raio: "))

pi = 3.14159
densidade_agua = 1.0

volume = pi * (raio ** 2) * altura
densidade_objeto = massa / volume

if densidade_objeto < densidade_agua:
    print(f"O objeto vai boiar ({densidade_objeto:.6f})")
else:
    print(f"O objeto não vai boiar ({densidade_objeto:.6f})")