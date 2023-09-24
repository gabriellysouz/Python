#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
    if p == 1:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(' ')
print('O maior peso digitado foi {}kg'.format(maior))
print('O menor peso digitado foi {}kg'.format(menor))
