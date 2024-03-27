#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.


class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    @property
    def saudacao(self):
        return f'Ola, {self.profissao}, tenha uma otima semana'
    


pessoa1 = Pessoa('lucas', 32, 'dev')
pessoa1.aniversario()
pessoa1.aniversario()

print(pessoa1)
print(pessoa1.saudacao)

