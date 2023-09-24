# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont = cont +1
        print('\033[1;33m'+str(c)+'\033[m', end=' ')
    else:
        print('\033[1;31m' + str(c) + '\033[m', end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(num, cont))
if cont == 2:
    print('Por isso É PRIMO')
else:
    print('Por isso NAO É PRIMO')
