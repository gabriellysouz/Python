#Exercício Python 081: Crie um programa que vai ler vários números e
# colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
flag = 'Ss'
cont = 0
while flag not in 'Nn':
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    flag = str(input('Quer continuar (S/N)?'))
print(f'Foram digitados {cont} numeros')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta na lista')