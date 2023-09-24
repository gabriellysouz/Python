#Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela,
# com a formatação correta.


matriz = [[], [], []]
for m in range(0, 3):
    for n in range(0, 3):
        num = int(input(f'Digite um valor para [{m}/{n}]: '))
        matriz[m].append(num)
print('-=' * 20)
for lista in matriz:
    for numero in lista:
        print('[{:^5}]'.format(numero), end=' ')
    print()


