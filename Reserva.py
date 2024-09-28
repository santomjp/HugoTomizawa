nomes = []
destinos = []
continua = "Sim"

while continua == "Sim":
    nome = input("Digite o nome do passageiro: ")
    nomes.append(nome)

    destino = input("Digite o local de destino: ")
    destinos.append(destino)

    continua = input("Deseja continuar? (Sim/Não)")

for i in range(len(nomes)):
    print(f"{i + 1} - {nomes[i]}, destino: {destinos[i]}.")