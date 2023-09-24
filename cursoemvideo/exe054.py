#Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for p in range(1, 8):
    ano = int(input('Ano de nascimento da {}º pessoa: '.format(p)))
    idade = atual - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))


