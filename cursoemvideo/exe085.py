#Crie um programa onde o usuário possa digitar sete valores
#numéricos e cadastre-os em uma lista única que mantenha
#separados os valores pares e ímpares. No final, mostre os valores
#pares e ímpares em ordem crescente.


numero = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        numero[0].append(num)
    else:
        numero[1].append(num)
print('-' * 30)
numero[0].sort()
print(f'Os numeros pares digitados foram {numero[0]}')
numero[1].sort()
print(f'Os numeros impares digitados foram {numero[1]}')
