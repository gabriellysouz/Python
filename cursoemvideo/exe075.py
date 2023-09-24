#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

'''num = tuple(int(input('Digite um numero: ')) for c in range(1, 5))
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O numero 3 nao foi digitado nenhuma vez')
else:
    print(f'O numero 3 foi digitado na posição {num.index(3)+1}')
print(f'Os numeros pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=', ')'''


#resolução guanabara
num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O numero 3 nao foi digitado nenhuma vez')
else:
    print(f'O numero 3 foi digitado na posição {num.index(3)+1}')
print(f'Os numeros pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=', ')





