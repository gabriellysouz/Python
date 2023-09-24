import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(valor, 10)}')
print(f'Aumentando 10% temos R${moeda.aumentar(valor, 10)}')
