class Pessoa:
    def __init__(self,*filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return  f'Olá {id(self)}'

if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    osmar = Pessoa(felipe, nome='Osmar')
    print(Pessoa.cumprimentar(osmar))
    print(id(osmar))
    print(osmar.cumprimentar())
    print(osmar.nome)
    print(osmar.idade)
    for filho in osmar.filhos:
        print(filho.nome)
    osmar.sobrenome = 'Fernandes'
    del osmar.filhos
    print(osmar.__dict__)
    print(felipe.__dict__)


