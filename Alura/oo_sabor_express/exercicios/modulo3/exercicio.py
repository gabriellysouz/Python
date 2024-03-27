#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

class ContaBancaria:
    def __init__(self, titular='', saldo=0):
      self.titular = titular.title()
      self.saldo = saldo
      self.ativo = False
    
    def __str__(self):
       if self.ativo:
          return f'{self.titular} | R${self.saldo:.2f} | Ativo'
       else:
          return f'{self.titular} | R${self.saldo:.2f}'
    @classmethod
    def ativar_conta(cls, conta):
       conta.ativo = not conta.ativo


pessoa1 =ContaBancaria('lucas', 10)
pessoa2 =ContaBancaria('Hashi', 325)

ContaBancaria.ativar_conta(pessoa1)

print(pessoa1)
print(pessoa2)

 