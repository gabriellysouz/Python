#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('*' * 5, 'Loja', '*' * 5)
preço = float(input('Preço do produto: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/pix \n[2] à vista cartão \n[3] 2x no cartao '
      '\n[4] 3x ou mais no cartao')
opçao = int(input('Sua opção: '))
if opçao == 1:
    valordesc = (preço/100)*10
    desconto = preço - valordesc
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, desconto))
elif opçao == 2:
    valordesc = preço/100*5
    desconto = preço - valordesc
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, desconto))
elif opçao == 3:
    valor = preço/2
    print('Sua compra de R${:.2f} sera parcelada em 2 vezes de R${:.2f} sem juros'.format(preço, valor))
elif opçao == 4:
    vezes = int(input('Quantas parcelas: '))
    valordesc = (preço/100)*20
    juros = preço + valordesc
    parcela = juros/vezes
    print('Sua compra sera parcelada em {}x de R${:.2f} com juros'.format(vezes, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, juros))
else:
    print('Opção invalida')
