def calcularimc(peso, altura):
    resultado = peso / (altura * altura)
    return resultado


peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))
imc = calcularimc(peso, altura)
print('imc: ', imc)
