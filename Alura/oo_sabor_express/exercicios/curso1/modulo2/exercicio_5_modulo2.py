#Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome='', idade=0, cargo='', civil=''):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.civil = civil
    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} anos | Cago: {self.cargo} | Estado Civil: {self.civil}'
    


clt1 = Cliente('Mauro', 32, 'Gerente', 'Casado')
clt2 = Cliente('Barbara', 24, 'Assistente', 'Solteira')
clt3 = Cliente('Joana', 52, 'Diretora', 'Casada')

print(clt1)
print()
print(clt2)
print()
print(clt3)