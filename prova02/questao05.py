def triangulo(x, y, z):
    if x != y and x != z and y != z:
        return 1
    elif x == y and x != z:
        return 2
    elif x == z and x != y:
        return 2
    elif y == z and y != x:
        return 2
    else:
        return 3


lado1 = int(input("Primeiro lado: "))
lado2 = int(input("Segundo lado: "))
lado3 = int(input("Terceiro lado: "))

resultado = triangulo(lado1, lado2, lado3)
print(resultado)
