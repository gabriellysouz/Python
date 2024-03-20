#2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
#3 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.


class Restaurante:
    def __init__(self, nome, categoria, delivery, takeaway):
        self.nome = nome
        self.categoria = categoria
        self.delivery = delivery
        self.takeaway = takeaway
        self.status = False

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Delivery: {self.delivery} | Take Away: {self.takeaway} | Status: {self.status}'


rest_praca = Restaurante('Praça', 'Gourmet', 'Nao', 'Sim')
rest_pizza = Restaurante('Pizza Express', 'Fast Food', 'Sim', 'Sim' )
rest_brasaria = Restaurante('Brasaria', 'Portuguesa', 'Nao', 'Sim')

print(rest_brasaria)
print()
print(rest_pizza)
print()
print(rest_praca)