class Pessoa:
    def __init__(self, nome = None, idade = 20 ):
        self.idade= idade
        self.nome = nome
    def cumprimentar(self):
        return 'Ola, tudo bem ?'

if __name__ == '__main__':
    p = Pessoa('Felipe')
    print(p.cumprimentar())
    print(f'Me chamo {p.nome}')
    print(f'Tenho {p.idade} anos de idade')