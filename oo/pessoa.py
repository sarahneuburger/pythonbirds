class Pessoa:
    olhos = 2 #atributo de classe, padrão, default#

    def __init__(self, *filhos, nome=None, idade=25):
        self.nome = nome #none = nulo#
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá{id(self)}"

    @staticmethod #Método de classe - decorator#
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} - olhos {cls.olhos}"



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
    henrique.olhos = 1
    print(henrique.__dict__)
    print(helena.__dict__)
    print(Pessoa.olhos)
    print(henrique.olhos)
    print(helena.olhos)
    print(id(Pessoa.olhos), id(henrique.olhos), id(helena.olhos))
    print(Pessoa.metodo_estatico(), henrique.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), henrique.nome_e_atributos_de_classe())

