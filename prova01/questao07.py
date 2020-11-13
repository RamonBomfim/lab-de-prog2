vendas = []
valor_total = 0.0
produtos_vendidos = 0


def menu():
    print("****************************************")
    print("* i : Efetuar nova venda               *")
    print("* l : Lista de produtos vendidos       *")
    print("* b : Valor total das vendas           *")
    print("* e : Quantidade de produtos vendidos  *")
    print("* s : Valor médio de vendas            *")
    print("****************************************")


while True:
    menu()
    operacao = input(
        "O que deseja fazer? (Digite 'SAIR' se quiser encerrar)\n").lower()

    if operacao == 'sair':
        print("Encerrando...")
        break

    if operacao == 'i':
        modelo = input("Qual o modelo do produto?\n")
        valor = float(input("Qual o valor do produto?\nR$ \n"))
        valor_total += valor
        produtos_vendidos += 1
        vendas.append(modelo)

    if operacao == 'l':
        print(f"\nEstes foram os itens vendidos hoje: {vendas}\n")

    if operacao == 'b':
        print(f"\nEste é o valor total das vendas de hoje: R$ {valor_total}\n")

    if operacao == 'e':
        print(f"\nHoje vendemos {produtos_vendidos} produtos.\n")

    if operacao == 's':
        media = valor_total / produtos_vendidos
        print(f"\nO valor médio das vendas foi: R$ {media}\n")
