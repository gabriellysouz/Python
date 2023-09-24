#Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5
# números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numero = []
def sorteia():
    for n in range(0, 5):
        num = randint(0, 10)
        numero.append(num)
    print(f'Os numeros sorteados foram:',numero)
def somapar():
    soma = 0
    print(f'Entre os sorteados temos os seguintes numeros pares: ', end='')
    for n in numero:
        if n % 2 == 0:
            soma += n
            print( n, end=' ')
    print()
    print(f'E a soma entre eles é',soma)


sorteia()
somapar()
