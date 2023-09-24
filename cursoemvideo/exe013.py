sa = float(input('Indique o salario atual: R$'))
r = sa*15/100
sn = sa + r
print('De acordo com seu salario atual de R${:.2f}, \no valor com o reajuste de 15% é de R${:.2f}.'.format(sa,sn))
