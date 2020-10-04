salario = float(input("Informe o seu salário: "))

if salario > 1000:
    imposto = salario * 0.1
    print(f"Você deve pagar R$ {imposto:.2f} de imposto.")
elif salario <= 0:
    print("Digite um salário válido! (Maior que 0)")
else:
    imposto = salario * 0.05
    print(f"Você deve pagar R$ {imposto:.2f} de imposto")
