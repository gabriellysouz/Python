#Em um arquivo chamado main.py, importe a classe Carro.
#No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.


from veiculo import Carro

carro1 = Carro("Ford", "Focus", "Preto")
carro2 = Carro("Chevrolet", "Cruze", "Prata")
carro3 = Carro("Honda", "Civic", "Vermelho")

carros =[carro1, carro2, carro3]

for c in carros:
    print(f'{c.nome} | {c.modelo} | {c.cor} | {c.ligar()}')


