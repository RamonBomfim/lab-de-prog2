estado_civil = input("Informe se você é Solteiro ou Casado: ").lower()
salario = float(input("Informe o seu salário: R$ "))

if estado_civil == 'solteiro':
    imposto = salario * 0.1
    print(f"Você deve pagar R$ {imposto} de imposto.")
elif estado_civil == 'casado':
    imposto = salario * 0.09
    print(f"Você deve pagar R$ {imposto} de imposto.")
else:
    print("Por favor, informe seu estado civil corretamente.")
