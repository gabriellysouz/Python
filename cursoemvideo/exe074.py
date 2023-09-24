#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

'''from random import randint
sorteio = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os numeros sorteados foram: ', end='')
maior = 0
menor = 0
for s in sorteio:
    print(s, end=', ')
    if menor == 0 and maior == 0:
        menor = s
        maior = s
    else:
        if s > maior:
            maior = s
        if s < menor:
            menor = s
print(f'\nO maior numero é {maior}')
print(f'O menor nuemro é {menor}')'''


#usando metodo max a min
from random import randint
sorteio = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os numeros sorteados foram: ', end='')
for s in sorteio:
    print(s, end=', ')
print(f'\nO maior numero é {max(sorteio)}')
print(f'O menor nuemro é {min(sorteio)}')
