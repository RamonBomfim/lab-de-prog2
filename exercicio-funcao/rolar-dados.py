import random


class SimuladorDeDados:
    def __init__(self):
        self.face_minima = 1
        self.face_maxima = 6
        self.palpite = 0
        self.somatorio_dados = 0
        self.quantidade = 0

    def Iniciar(self):
        try:
            self.quantidade = int(
                input("Escolha de 1 a 4 dados para rolar:\n"))
        except ValueError:
            print("Digite apenas números inteiros entre 1 e 4!")
            self.Iniciar()

        self.PalpiteDoUsuario()

        for i in range(self.quantidade):
            self.somatorio_dados += self.GerarValor()

        print(f"Você chutou: {self.palpite}")
        print(f"O somatório final foi: {self.somatorio_dados}")

        if (self.palpite == self.somatorio_dados):
            print("Parabéns, você é muito bom de chute e acertou!")
        else:
            print("Como diria Raul Seixas: tente outra vez...")

    def PalpiteDoUsuario(self):
        try:
            self.palpite = int(input("Informe seu palpite:\n"))
        except ValueError:
            print("Você deve digitar apenas números inteiros!")
            self.PalpiteDoUsuario()

    def GerarValor(self):
        return random.randint(self.face_minima, self.face_maxima)


iniciar_jogo = SimuladorDeDados()
iniciar_jogo.Iniciar()
