p = float(input('Valor do produto: R$'))
d = p*5/100
t = p - d
print('O produto que custava R${:.2f}, com 5% de desconto é igual a R${:.2f}.'.format(p,t))

