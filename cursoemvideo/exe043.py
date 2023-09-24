#Desenvolva uma lógica que leia o peso e a altura de
# uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso (kg)? '))
altura = float(input('Qual seu altura (m)? '))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso')
elif imc < 25:
    print('Voce esta no peso ideal')
elif imc < 30:
    print('voce esta em sobrepeso')
elif imc < 40:
    print('voce esta em obesidade ')
else:
    print('Voce esta em obesidade morbida')