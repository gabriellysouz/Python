import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formoeda(valor)} é {moeda.formoeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.formoeda(valor)} é {moeda.formoeda(moeda.dobro(valor))}')
print(f'Diminuindo 10%, temos {moeda.formoeda(moeda.diminuir(valor, 10))}')
print(f'Aumentando 10% temos {moeda.formoeda(moeda.aumentar(valor, 10))}')
