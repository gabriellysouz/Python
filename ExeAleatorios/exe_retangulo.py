# Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
# de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valor_ladoA(self, novo_ladoA):
        self.ladoA = novo_ladoA

    def mudar_valor_ladoB(self, novo_ladoB):
        self.ladoB = novo_ladoB

    def retornar_valor(self):
        print(f'Lado A: {self.ladoA} | Lado B: {self.ladoB} | Area: {self.calcular_area()} '
              f'| Perimetro : {self.calcular_perimetro()}')

    def calcular_area(self):
        return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        return (self.ladoA*2) + (self.ladoB*2)


def pegar_variavel():
    lado1 = int(input('Indique o comprimento em cm: '))
    lado2 = int(input('indique a largura em cm: '))
    return Retangulo(lado1,lado2)

def main():
    print('Sobre o tamanho do comodo')
    obj_comodo = pegar_variavel()
    print('----------')
    print('Sobre o tamanho do piso')
    area_piso = pegar_variavel()
    print('----------')
    print('Para um comodo com as seguintes medidas: ')
    obj_comodo.retornar_valor()
    pisos_necessarios = obj_comodo.calcular_area() / area_piso.calcular_area()
    print(f'Serao necessarios {pisos_necessarios} pisos')

main()

