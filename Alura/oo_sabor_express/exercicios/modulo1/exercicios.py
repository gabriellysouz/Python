#projeto base

class Restaurante:
    nome = ''
    categoria = ''
    status = False


rest_praca = Restaurante()
rest_praca.nome = 'Praça'
rest_praca.categoria = 'Gourmet'

rest_pizza = Restaurante()
rest_pizza.nome = 'Pizza'
rest_pizza.categoria ='Fast Food'

restaurantes = [vars(rest_pizza), vars(rest_praca)]

print(restaurantes)
print('--------')

# 1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

rest_praca.categoria = 'Italiana'
print(restaurantes)
print('--------')

#2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

nome_rest = rest_praca.nome

#3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if rest_praca.status:
    print('Restaurante Praça : Ativo')
else:
    print('Restaurante Praça : Inativo')

print('--------')

if rest_pizza.status:
    print('Restaurante Pizza : Ativo')
else:
    print('Restaurante Pizza : Inativo')

#4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria
    
categoria = Restaurante.categoria

#5 - Altere o valor do atributo nome para 'Bistrô'.

rest_praca.categoria = 'Bistrô'
print(restaurantes)
print('--------')

#6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

rest_pizza_place = Restaurante()
rest_pizza_place.nome = 'Pizza Place'
rest_pizza_place.categoria = 'Fast Food'

restaurantes.append(vars(rest_pizza_place))
print(restaurantes)
print('--------')

#7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if rest_pizza.categoria == 'Fast Food':
    print('Restaurante Pizza é da categoria fast food')
else:
    print('Restaurante Pizza NAO é da categoria fast food')

#8 - Mude o estado da instância restaurante_pizza para ativo. 

rest_pizza.status = True

#9 - Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'Nome: {rest_praca.nome}, Categoria: {rest_praca.categoria}')