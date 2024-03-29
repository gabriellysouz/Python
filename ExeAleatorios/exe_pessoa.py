# Crie uma classe que modele uma pessoa:
#
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome.title()
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.crescer()

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self):
        self.altura += 0.5

    def mostrar_info(self):
        print(f'Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso}kg| Altura: {self.altura}cm')


pessoa1 = Pessoa('jose', 20, 80, 180)
pessoa1.mostrar_info()
pessoa1.envelhecer()
pessoa1.mostrar_info()
pessoa1.envelhecer()
pessoa1.mostrar_info()
pessoa1.emagrecer(5)
pessoa1.mostrar_info()
pessoa1.engordar(3)
pessoa1.mostrar_info()












