lista = []
naoContinua = int(input("Digite um número: "))
lista.append(naoContinua)

while naoContinua != 0:
    naoContinua = int(input("Digite um número: "))
    lista.append(naoContinua)

ordem = input("Deseja organizar a lista em ordem crescente ou decrescente?\n")

if ordem.upper() == "CRESCENTE":
    for i in range(len(lista)):
        while lista[i] >= lista[i + 1]:
            c = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = c


print(lista)