#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

lista_num = [1,2,3,4,5,6,7,8,9,10]
impares =[]
soma = 0

for n in lista_num:
    if n % 2 != 0:
        impares.append(n)
        soma += n
print('De 0 a 10, os numeros impares sao: ')
for n in impares:
    print(f'.{n} ', end='')

print(f'\nA soma desses numero é igual a {soma}')
