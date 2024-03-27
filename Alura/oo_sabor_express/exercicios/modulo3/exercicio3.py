#Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

#Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:
    def __init__(self, nome, cargo, saldo, cpf,email):
        self._nome = nome
        self._cargo = cargo
        self._saldo = saldo
        self._cpf = cpf
        self._email = email
    def __str__(self):
        return f'Nome: {self._nome} | Cargo: {self._cargo} | Saldo: R${self._saldo:.2f} | CPF: {self._cpf} | E-mail: {self._email} '
    @classmethod
    def saldo_cliente(cls, titular, saldo):
        return f'{titular} | Saldo: R${saldo:.2f}'

    

cliente1 = ClienteBanco('Ana Sousa', 'Gerente', 2250, '231.548.632-33', 'ana.sousa@gamil.com')
cliente2 = ClienteBanco("Luiza","Diretora", 5126,"987.654.321-01", "luiza@gmail.com")
cliente3 = ClienteBanco("Vinny Neves","Assistente", 1520, "111.222.333-44", "vinny.12@gamil.com")


cliente1 = ClienteBanco.saldo_cliente('Ana Sousa', 2250)
print(cliente1)

