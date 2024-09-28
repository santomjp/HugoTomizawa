nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

#para arredondar resultado para 2 casas decimais
imc = round((peso / altura**2),2)

print(f"Olá, {nome}! \nSeu IMC é: {imc}.")

#ou para esconder as casas decimais e mostrar apenas 2 -> :.2f
#imc = round((peso / altura**2),2)
#print(f"Olá, {nome}! \nSeu IMC é: {imc:.2f}.")