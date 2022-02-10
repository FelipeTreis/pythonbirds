class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 20):
        self.idade= idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return 'Ola, tudo bem ?'

if __name__ == '__main__':
    renzo = Pessoa(nome = 'Renzo')
    felipe = Pessoa(renzo, nome = 'Felipe')
    print(felipe.cumprimentar())
    print(f'Me chamo {felipe.nome}')
    print(f'Tenho {felipe.idade} anos de idade')
    print(f'{id(Pessoa)}')

    for filho in felipe.filhos:
        print(filho.nome)

