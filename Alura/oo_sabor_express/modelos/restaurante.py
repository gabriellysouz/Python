from modelos.avaliacao import Avaliacao

class Restaurante:
    list_rest = []

    def __init__(self, nome, categoria):  #construtor 
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False  #atributo fica protegido, nao é ser modificado fora da classe
        self._avaliacao = []
        Restaurante.list_rest.append(self)
    
    def __str__(self):   #retorna objeto em texto 
        return f'{self._nome} | {self._categoria}'
    
    @classmethod  #informaçao referente a classe 
    def listar_restaurante(cls):
        for rest in cls.list_rest:
            print(f'{rest._nome.ljust(15)} | {rest._categoria.ljust(15)} | {str(rest.media_aval).ljust(15)} | {rest.status}')
    
    @property #modifica uma propriedade em especifico 
    def status(self):
        return 'Ativo' if self._status else 'Inativo'

    def alternar_status(self):
        self._status = not self._status

    def receber_aval(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_aval(self):
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quant_nota = len(self._avaliacao)
        media = round(soma_notas/quant_nota, 1)
        return media 

 
 