lista = []
contador = 1

while contador <= 5:
    numero = float(input("Digite um número: "))
    lista.append(numero)

    contador += 1

#print(lista)

soma = 0
for i in range(len(lista)):
#    print(lista[i], end=" ")
    soma += lista[i]

print(f"A soma dos números digitados é: {soma}")