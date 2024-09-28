nota = float(input("Insira sua nota:"))

if 90 <= nota <= 100:
    print("Classificação: A")
elif 80 <= nota < 90:
    print("Classificação: B")
elif 70 <= nota < 79:
    print("Classificação: C")
elif 60 <= nota < 69:
    print("Classificação: D")
elif 0 <= nota < 60:
    print("Classificação: F")
else:
    print("Valor inválido.")