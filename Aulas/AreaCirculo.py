raioCirc = float(input("Digite o raio do círculo em centímetros: "))
import math
import matplotlib

areaCirc = round(math.pi* raioCirc**2,4)

print(f"A área do círculo é {areaCirc} cm²")