salario = float(input("Informe seu salário atual: R$"))
tempo = int(input("Informe quantos anos de serviço você possui:"))

if tempo > 5:
    print(f"Bônus salarial: 5% \nSalário atualizado: R${salario * 0.05}")
else:
    print(f"Bônus salarial: 0% \nSalário: R${salario}")