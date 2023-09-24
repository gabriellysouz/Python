#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer
# qual deles é o maior.

def maior(*num):
    print('-' * 30)
    print('Analisando os valores passados...')
    maior = cont = 0
    for c in num:
        print(f'{c}', end=' ')
        cont += 1
        if c > maior:
            maior = c
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor informado é {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(4, 2, 7, 1, 10, 3)
