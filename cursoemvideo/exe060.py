#Exercício Python 060: Faça um programa que leia um número qualquer e
# mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''num = int(input('Digite um numero para calcular seu fatorial: '))
resul = 1
print('Calculando {}! ='.format(num), end=' ')
for c in range(num, 1, -1):
    resul = resul * c
    print(c, end=' x ')
print('1 = {}'.format(resul))'''

num = int(input('Digite um numero para calcular seu fatorial: '))
print('Calculando {}! ='.format(num), end=' ')
resul =1
num1 = num + 1
while num1 != 2:
    num1 -= 1
    resul = resul * num1
    print(num1, end=' x ')
print('1 = {}'.format(resul))


