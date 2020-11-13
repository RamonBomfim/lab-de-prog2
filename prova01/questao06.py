from pprint import pprint

print("Descubra a tabuada do número que desejar\n")


def Tabuadas():
    numero = int(
        input("Digite o número ao qual deseja saber sua tabuada: "))
    cont = 0

    if numero >= 0:
        while cont <= 10:
            tabuada_mult = numero * cont
            tabuada_adi = numero + cont
            pprint("%d x %d = %d" % (numero, cont, tabuada_mult))
            pprint("%d + %d = %d" % (numero, cont, tabuada_adi))
            cont += 1


Tabuadas()
