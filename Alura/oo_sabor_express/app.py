from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

rest_praca = Restaurante('praça', 'gourmet')

suco_melancia = Bebida('Suco de Melancia', 5.0, 'Grande')
paozinho = Prato('Paozinho', 2.0, 'Melhor pao da cidade')



def main():
    print(suco_melancia)
    print(paozinho)


if __name__ == '__main__':
    main()


