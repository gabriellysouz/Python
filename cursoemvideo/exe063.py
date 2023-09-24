#Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.
print('Sequencia de Fibonacci')
print('-' * 15)
n = int(input('Quantos termos voce quer mostrar?  '))
t1 = 0
t2 = 1
count = 3
print('{} -> {} -> '.format(t1, t2), end='')
while count <= n:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    count += 1
print('Fim')