import random

numeros_sorteados = []

quantidade_numeros = int(
    input("Olá! Informe quantos núemros pretende jogar:\n"))
numeros_do_jogo = []

for jogo in range(quantidade_numeros):
    jogo = int(input("Digite os números que deseja jogar:\n"))
    numeros_do_jogo.append(jogo)

for sorteio in range(6):
    numero_sorteado = random.randrange(1, 61)
    if numero_sorteado not in numeros_sorteados:
        numeros_sorteados.append(numero_sorteado)

numero_de_acertos = [
    certos for certos in numeros_sorteados if certos in numeros_do_jogo]

print(f"Os números sorteados foram: {numeros_sorteados}")
print(f"Você acertou os números {numero_de_acertos}")

if len(numero_de_acertos) == 4:
    print("Você fez uma quadra!")
elif len(numero_de_acertos) == 5:
    print("Você fez uma quina!")
elif len(numero_de_acertos) == 6:
    print("Parabéns você fez uma sena, está rico!")
else:
    print("Tente a sorte outra vez!")
