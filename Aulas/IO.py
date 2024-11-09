nome = input("Digite seu nome: ")

print("Olá, " + nome + "!")
#Sinal de + ñ adiciona espaço entre palavras

print("Olá,", nome, "!")
#Sinal de , adiciona espaço entre palavras

print("Olá,", nome + "!")
print("Olá, %s!" %nome)
#Sinal % é uma forma antiga de formatar strings

print("Olá, {}!".format(nome))
#.format() é uma forma mais moderna de formatar strings

print(f"Olá, {nome}!")
#f-string é a forma mais moderna de formatar strings

numeroUm = int(input("Digite um número inteiro: "))

print(numeroUm + 10)

numeroDois = float(input("Digite outro número qualquer: "))

print(numeroUm + numeroDois)

numeroTres = float(input("Digite outro número qualquer: "))
numeroQuatro = float(input("Digite um último número qualquer: "))

adicao = numeroUm + numeroDois + numeroTres + numeroQuatro
subtracao = numeroUm - numeroDois - numeroTres - numeroQuatro
multiplicacao = numeroUm * numeroDois * numeroTres * numeroQuatro
divisao = numeroUm / numeroDois / numeroTres / numeroQuatro

print("     Resultados")
print("-" * 40)
print(f"Soma: {adicao}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")