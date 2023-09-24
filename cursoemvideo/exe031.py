viagem = float(input('Qual a distancia da viagem em Km? '))
longa = viagem * 0.45
curta = viagem * 0.50
if viagem <= 200:
    print('O valor da sua viagem é de R${:.2f}'.format(curta))
else:
    print('O valor da sua viagem é de R${:.2f}'.format(longa))
print('Boa viagem!')
