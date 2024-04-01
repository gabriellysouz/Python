#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

#Crie uma instância da classe e imprima o valor da propriedade titular.

class ContaBancaria:
    def __init__(self, titular='',saldo=0):
        self._titular = titular.title()
        self._saldo = saldo
        self._status = False
    def __str__(self):
        if self._status:
          return f'{self._titular.ljust(20)} | R${self._saldo.ljust(20):.2f} | Ativo'
        else:
            return f'{self._titular.ljust(20)} | R${self._saldo:.2f}'
    @classmethod
    def ativar_conta(cls,conta):
        conta._status = not conta._status
    @property
    def titular_conta(self):
        return f'{self._titular}'


pessoa1 =ContaBancaria('lucas', 10)
pessoa2 =ContaBancaria('Hashi', 325)

print(pessoa2.titular_conta)

