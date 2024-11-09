import math

print("Tipos de reforma:\n- Simples;\n- Completa;\n- Luxo.")
tipoReforma = input("Informe o tipo de reforma:")
print("*" * 30)

print("Tipos de materiais:\n- Padrão;\n- Premium;\n- Luxo.")
tipoMaterial = input("Informe o tipo de material utilizado:")
print("*" * 30)

tamanhoReforma =  float(input("Informe o tamanho da reforma em m²:"))
print("*" * 30)

print("Localização:\n- Central;\n- Periférica.")
localizacao = input("Informe a localização da reforma:")
print("*" * 30)

if tamanhoReforma <= 0:
    print("Número inválido!")

if tipoReforma.upper() == "Simples":
    precoReforma = tamanhoReforma * 300
elif tipoReforma == "Completa":
    precoReforma = tamanhoReforma * 500
elif tipoReforma == "Luxo":
    precoReforma = tamanhoReforma * 800

if tipoMaterial == "Padrão":
    descontoMaterial = 0
elif tipoMaterial == "Premium":
    descontoMaterial = precoReforma * 0.2
elif tipoMaterial == "Luxo":
    descontoMaterial = precoReforma * 0.5

if tamanhoReforma > 100:
    descontoTamanho = precoReforma * 0.1
elif tamanhoReforma < 30:
    descontoTamanho = - precoReforma * 1.15
else:
    descontoTamanho = 0

if tamanhoReforma > 150:
    precoEquipe = 2000 * (math.ceil((tamanhoReforma - 150) / 50))
else:
    precoEquipe = 0

if localizacao == "Central":
    precoFinal = precoReforma + descontoMaterial - (descontoTamanho) + precoEquipe + 5000
elif localizacao == "Periférica":
    precoFinal = precoReforma + descontoMaterial - (descontoTamanho) + precoEquipe + 3000

print(f"O preço final da reforma é: R${precoFinal:.2f}")