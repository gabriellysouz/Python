from modelos.restaurante import Restaurante

rest_praca = Restaurante('praça', 'gourmet')
rest_pizza = Restaurante('pizza express', 'fast food')

rest_brasaria = Restaurante('brasaria', 'portuguesa')
rest_brasaria.receber_aval('nata', 6)
rest_brasaria.receber_aval('hashi', 4)
rest_brasaria.receber_aval('lucas', 8)


def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()


