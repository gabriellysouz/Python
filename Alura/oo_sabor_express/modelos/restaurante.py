class Restaurante:
    list_rest = []

    def __init__(self, nome, categoria):  #construtor 
        self.nome = nome
        self.categoria = categoria
        self._status = False  #atributo fica protegido, nao deve ser modificado
        Restaurante.list_rest.append(self)
    
    def __str__(self):   #retorna objeto em texto 
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurante():
        for rest in Restaurante.list_rest:
            print(f'{rest.nome} | {rest.categoria} | {rest.status}')
    
    @property #modifica uma propriedade em especifico 
    def status(self):
        return 'Ativo' if self._status else 'Inativo'



rest_praca = Restaurante('Praça', 'Gourmet')
rest_pizza = Restaurante('Pizza Express', 'Fast Food')
rest_brasaria = Restaurante('Brasaria', 'Portuguesa')


Restaurante.listar_restaurante()

