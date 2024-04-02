#Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
#No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, nome, modelo):
        self.nome = nome
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

#Crie uma nova classe chamada Carro que herda da classe Veiculo.
#No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
    
class Carro(Veiculo):
    def __init__(self, nome, modelo, cor):
        super().__init__(nome, modelo)
        self.cor = cor
    def ligar(self):
        return 'Ligado'