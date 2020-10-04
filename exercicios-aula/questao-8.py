clientes = 3
codigo_alto = 0
codigo_baixo = 0
codigo_pesado = 0
codigo_leve = 0
mais_alto = 0.0
mais_baixo = 10000.0
mais_pesado = 0.0
menos_pesado = 10000.0
media_peso = 0.0
media_altura = 0.0

for i in range(clientes):
    codigo = int(input("Qual seu código de matrícula?\n"))
    altura = float(input("Qual a sua altura?\n"))
    peso = float(input("Quanto você pesa?\n"))

    media_altura += altura
    media_peso += peso

    if (altura > mais_alto):
        codigo_alto = codigo
        mais_alto = altura
    elif (altura < mais_baixo):
        codigo_baixo = codigo
        mais_baixo = altura

    if (peso > mais_pesado):
        codigo_pesado = codigo
        mais_pesado = peso
    elif (peso < menos_pesado):
        codigo_leve = codigo
        menos_pesado = peso

print(f'O cliente mais alto é o de código {codigo_alto} com {mais_alto}m')
print(f'O cliente mais baixo é o de código {codigo_baixo} com {mais_baixo}m')
print(
    f'O cliente mais pesado é o de código {codigo_pesado} com {mais_pesado}kg')
print(f'O cliente mais leve é o de código {codigo_leve} com {menos_pesado}kg')
print(f'A média de peso da academia é {media_peso / clientes:.2f}kg')
print(f'A média de altura da academia é {media_altura / clientes:.2f}m')
