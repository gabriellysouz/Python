print('-' * 20)
print('CONTINENTE')
print('-' *20)
total = 0
maiormil = 0
menor = 0
produmenor = ''
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if menor == 0:
        menor = preco
    elif preco < menor:
        menor = preco
        produmenor = produto
    elif preco >= 1000:
        maiormil += 1
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Quer continuar? (S/N) ')).upper().strip()[0]
    if conti == 'N':
        break
print('----- FIM -----')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maiormil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {produmenor} que custa {menor:.2f}')
