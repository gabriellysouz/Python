# Crie uma classe que modele uma bola: Atributos: Cor, circunferência, material Métodos: trocaCor e mostraCor

class Bola:
    bolas = []

    def __init__(self, cor = '', material = '', circunferencia = 0):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        Bola.bolas.append(self)
    
    def trocar_cor(self, novaCor):
        self.cor = novaCor
    
    def mostrar_info(self):
        print(f'Circunferencia: {self.circunferencia} cm | Cor: {self.cor} | Material: {self.material} ')
    
    def mostrar_cor(self):
        print(f'A cor da bola é {self.cor}')

    @classmethod
    def ver_bolas(cls):
        print('------------------')
        for b in cls.bolas:
            print(f'Circunferencia: {b.circunferencia} cm | Cor: {b.cor} | Material: {b.material} ')

def menu():
    print('------------------')
    print('Menu')
    print('1 - Adicionar Bola')
    print('2 - Listar Bolas')
    print('3 - Sair')
    print('------------------')


def criando_bola():
    print('------------------')
    cor = input('Digite a cor: ')
    material = input('Indique o material: ')
    circun = int(input('Digite a circunferencia em cm: '))
    return Bola(cor, material, circun)



op = 0
while op != 3:
    menu()
    op = int(input('Indique opção pretendida: '))
    if op == 1:
        criando_bola()
    elif op == 2:
        Bola.ver_bolas()

print('Adeus')







