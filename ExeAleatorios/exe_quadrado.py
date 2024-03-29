# Crie uma classe que modele um quadrado:  Atributos: Tamanho do lado  Métodos: Mudar valor do Lado,
# Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tam_lado):
        self.tam_lado = tam_lado

    def mudar_tam(self, novo_tam):
        self.tam_lado = novo_tam

    def calc_area(self):
        return self.tam_lado * self.tam_lado

def criar_quadrado():
    lado = Quadrado(int(input('Digite o tamanho do lado do quadrado: ')))
    print(f'A area do quadrado é igual a {lado.calc_area()}')
    print('------')
    novo_tamanho()

def novo_tamanho ():
    while True:
        cont = int(input('Digite 1 para alterar o tamanho do lado - '))
        print('----------')
        if cont == 1:
            criar_quadrado()
        else:
            break

criar_quadrado()
print('Adeus')




