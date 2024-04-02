from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

rest_praca = Restaurante('praça', 'gourmet')

suco_melancia = Bebida('Suco de Melancia', 5.0, 'Grande')
suco_melancia.aplicar_desconto()
paozinho = Prato('Paozinho', 2.0, 'Melhor pao da cidade')
paozinho.aplicar_desconto()
rest_praca.add_item_cardapio(suco_melancia)
rest_praca.add_item_cardapio(paozinho)



def main():
    rest_praca.exibir_cardapio

if __name__ == '__main__':
    main()


