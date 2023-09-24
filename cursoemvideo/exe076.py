#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 50)
print('{:^50}'.format('LISTA DE PREÇOS'))
print('-' * 50)
for p in produtos:
    if produtos.index(p) % 2 == 0:
        print('{:.<40}'.format(p), end='')
    else:
        print('R$', '{:>6.2f}'.format(p))
print('-' * 50)


