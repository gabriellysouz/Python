# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

num = int(input('Indique um numero para ver sua tabuada: '))

for n in range(1,11):
    print(f'{num} x {n} = {num*n}')


