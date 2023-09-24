#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
somapar = 0
maior2linha = 0
soma3coluna = 0
for m in range(0, 3):
    for n in range(0, 3):
        valor = int(input(f'Digite um valor para posição [{m}/{n}]: '))
        matriz[m].append(valor)
        if valor % 2 == 0:
            somapar+= valor
        if m == 1:
            if valor > maior2linha:
                maior2linha = valor
        if n == 2:
            soma3coluna += valor
print('-=' * 30)
for lista in matriz:
    for numero in lista:
        print('[{:^5}]'.format(numero), end='')
    print()
print('-=' * 30)
print(f'A soma dos numeros pares é de {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3coluna}')
print(f'O maior valor da segunda linha é {maior2linha}')
