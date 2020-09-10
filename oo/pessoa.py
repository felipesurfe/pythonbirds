class Pessoa:
    def __init__(self,*filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return  f'Olá {id(self)}'

if __name__ == '__main__':
    fernandes = Pessoa(nome='Fernandes')
    felipe = Pessoa(fernandes, nome='Felipe')
    print(Pessoa.cumprimentar(felipe))
    print(id(felipe))
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)
    for filho in felipe.filhos:
        print(filho.nome)


