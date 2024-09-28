valorInicial = float(input("Informe o preço do produto: R$"))
formaPagamento = int(input("Informe a forma de pagamento\nDigite 0 para pagamento à vista ou 1 para pagamento à prazo:\n"))

if formaPagamento == 0:
    if 0 <= valorInicial <= 500:
        print(f"Desconto de 10% concedido. Valor final: R${valorInicial * 0.9}.")
    elif 500 < valorInicial <= 1000:
        print(f"Desconto de 15% concedido. Valor final: R${valorInicial * 0.85}.")
    elif valorInicial > 1000:
        print(f"Desconto de 20% concedido. Valor final: R${valorInicial * 0.8}.")
else:
    if valorInicial <= 800:
        numeroParcelas = int(input(("Esse valor pode ser parcelado em até 5x.\nDigite o número de parcelas desejado:")))
        if numeroParcelas >= 5:
            print("Número de parcelas inválido.")
        else:
            print(f"Valor final: R${valorInicial}")
    elif valorInicial > 800:
            numeroParcelas = int(input("Esse valor pode ser parcelado em até 18x.\nDigite o número de parcelas desejado:"))
            if 0 < numeroParcelas <= 10:
                print(f"Valor final: R${valorInicial}.")
            elif 10 < numeroParcelas <= 18:
                if numeroParcelas == 11: valorFinal = valorInicial * 1.05;
                elif numeroParcelas == 12: valorFinal = valorInicial * 1.065;
                elif numeroParcelas == 13: valorFinal = valorInicial * 1.07;
                elif numeroParcelas == 14: valorFinal = valorInicial * 1.09;
                elif numeroParcelas == 15: valorFinal = valorInicial * 1.095;
                elif numeroParcelas == 16: valorFinal = valorInicial * 1.1;
                elif numeroParcelas == 17: valorFinal = valorInicial * 1.113;
                elif numeroParcelas == 18: valorFinal = valorInicial * 1.12;
            
                print(f"Valor final: R${valorFinal}")
            else:
                print("Número de parcelas inválido.")