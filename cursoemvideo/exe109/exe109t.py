import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formoeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.formoeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(valor, 10, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(valor, 10, True)}')
