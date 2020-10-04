salario = float(input("Informe quanto você recebe: R$ "))

if (salario < 1000):
    imposto = salario * 0.05
    print(f"O seu salário bruto é de R$ {salario}")
    print(f"Você precisa pagar R$ {imposto:.2f} de imposto")
    print(f"O seu salário liquido é de R$ {salario - imposto}")
elif (salario >= 1000) and (salario < 5000):
    imposto = salario * 0.11
    print(f"O seu salário bruto é de R$ {salario}")
    print(f"Você precisa pagar R$ {imposto:.2f} de imposto")
    print(f"O seu salário liquido é de R$ {salario - imposto}")
else:
    imposto = salario * 0.35
    print(f"O seu salário bruto é de R$ {salario}")
    print(f"Você precisa pagar R$ {imposto:.2f} de imposto")
    print(f"O seu salário liquido é de R$ {salario - imposto}")
