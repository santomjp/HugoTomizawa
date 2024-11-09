numero1 = float(input("Digite um número qualquer:"))
numero2 = float(input("Digite outro número qualquer:"))
operacao = input("Qual operação deseja fazer? (+, -, /, *)\n")

if operacao == "+":
    print(f"A soma é = {numero1 + numero2}")
elif operacao == "-":
    print(f"A subtração é = {numero1 - numero2}")
elif operacao == "/":
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(f"A divisão é = {numero1 / numero2}")
elif operacao == "*":
    print(f"A multiplicação é: {numero1*numero2}")
else:
    print("Esta não é uma operação válida.")
