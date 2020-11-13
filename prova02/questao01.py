def calcular(a, b):
    if (a > b):
        total = a * b
    elif (a == b):
        total = a * (b + 2)
    else:
        total = a

    print(total)


calcular(10, 10)
