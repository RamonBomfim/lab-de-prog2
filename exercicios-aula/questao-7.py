print("Digite S - Solteiro, C - Casado, N - Namorando,")
print("D - Divorciádo ou V - Viúvo")
estado_civil = input("Qual seu estado civil?\n").lower()

if estado_civil == 's':
    print("Solteiro")
elif estado_civil == 'c':
    print("Casado")
elif estado_civil == 'n':
    print("Namorando")
elif estado_civil == 'd':
    print("Divorciádo")
elif estado_civil == 'v':
    print("Viúvo")
else:
    print("Digite uma das letras da legenda!!")
