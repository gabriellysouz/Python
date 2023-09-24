vel = int(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel>80:
    print('MULTADO! Voce execeu o limite de 80 km/h')
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
