class Pessoa:
    def __init__(self, *filhos, nome=None, idade=25):
        self.nome = nome #none = nulo#
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá{id(self)}"

if __name__ == '__main__':
    helena = Pessoa(nome="Helena")
    henrique = Pessoa(helena, nome="Henrique")
    print(Pessoa.cumprimentar(henrique))
    print(id(henrique))
    print(henrique.cumprimentar())
    print(henrique.nome)
    print(henrique.idade)
    for filho in henrique.filhos:
        print(filho.nome)
    henrique.sobrenome = "Martins"
    print(henrique.sobrenome)
    del henrique.filhos
    print(henrique.__dict__)
    print(helena.__dict__)

