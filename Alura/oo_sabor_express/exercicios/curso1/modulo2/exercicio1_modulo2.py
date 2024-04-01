#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def __str__(self):
        return f'{self.modelo} | {self.modelo} | {self.ano}'

carro1 = Carro('Punto','Preto',2010)

print(carro1)
