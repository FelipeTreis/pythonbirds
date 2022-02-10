class Motor:
    def __init__(self, velocidade, acelerar, frear):
        self.velocidade = velocidade
        self.acelerar = acelerar
        self.frear = frear
        self.motor = Motor

    def acelerar(self):
        motor = Motor()

        motor.velocidade = 0

        motor.acelerar()
        motor.velocidade = 1

        motor.acelerar()
        motor.velocidade = 2

        motor.acelerar()
        motor.velocidade = 3

    def frear(self):
        motor = Motor()

        motor.frear()
        motor.velocidade = 1

        motor.frear()
        motor.velocidade = 3

class Direcao:
    def __init__(self, girar_direira, girar_esquerda):
        self.girar_direita = girar_direira
        self.girar_esquerda = girar_esquerda

    def girar_direita(self):
        direcao = Direcao()
        direcao.valor = 'norte'

        direcao.girar_direita()
        direcao.valor = 'leste'

        direcao.girar_direita()
        direcao.valor = 'sul'

        direcao.girar_direita()
        direcao.valor = 'oeste'

        direcao.girar_direita()
        direcao.valor = 'norte'

    def girar_esquerda(self):
        direcao = Direcao()
        direcao.valor = 'oeste'

        direcao.girar_esquerda()
        direcao.valor = 'sul'

        direcao.girar_esquerda()
        direcao.valor = 'leste'

        direcao.girar_esquerda()
        direcao.valor = 'norte'

class Carro:
    def __init__(self):
        self.carro = Carro(Direcao, Motor)



















