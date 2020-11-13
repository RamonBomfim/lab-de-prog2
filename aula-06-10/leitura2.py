arquivo = open('arquivo.txt', 'r')


lado1 = arquivo.readline()[0]
lado2 = arquivo.readlines()[2]
lado3 = arquivo.readlines()[4]

print(lado1)
print(lado2)
print(lado3)
