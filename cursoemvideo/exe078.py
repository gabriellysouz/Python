#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

numero = list()
maior = 0
menor = 0
for c in range(0, 5):
    numero.append(int(input(f'Digite um valor para a posição {c}: ')))
    for n in numero:
        if maior == 0 and menor == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print(f'Voce digitou os valores {numero}')
print(f'O menor numero digitado foi {menor} na posiçao ', end='')
for i, v in enumerate(numero):
    if v == maior:
        print(f'{i}..', end='')
print()
print(f'O maior numero digitado foi {maior} na posiçao ', end='')
for i, v in enumerate(numero):
    if v == menor:
        print(f'{i}..', end='')
