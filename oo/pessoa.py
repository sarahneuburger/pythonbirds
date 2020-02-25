class Pessoa:
    def __init__(self, nome=None, idade=25):
        self.nome = nome #none = nulo#

    def cumprimentar(self):
        return f"Olá{id(self)}"

if __name__ == '__main__':
    p = Pessoa("Henrique")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Sarah" #alterar valor do atributo#
    print(p.nome)
    print(p.idade)
