class Pessoa:
    olhos = 2 #atributo de classe, padrão, default#

    def __init__(self, *filhos, nome=None, idade=25):
        self.nome = nome #none = nulo#
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}"

    @staticmethod #Método de classe - decorator#
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} - olhos {cls.olhos}"


class Homem(Pessoa): #heranca simples, Homem herda de pessoa
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar() #sobrescrita de método
        return f"{cumprimentar_da_classe}. Aperto de mão."

class Mutante(Pessoa):
    olhos = 3 #sobreponto o atributo em relação a classe Pai Pessoa

if __name__ == '__main__':
    helena = Mutante(nome="Helena") #sobrescrita de dados
    henrique = Homem(helena, nome="Henrique")
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
    pessoa = Pessoa("Anonimo")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(henrique, Pessoa))
    print(isinstance(henrique, Homem))
    print(helena.olhos)
    print(henrique.cumprimentar())
    print(helena.cumprimentar())