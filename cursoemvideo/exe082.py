#Crie um programa que vai ler vários números e colocar
# em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

lista = []
par = []
impar = []
cont = 'Ss'
while cont not in 'Nn':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont = str(input('Deseja continuar (S/N)? '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('-' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')


#resolução guanabara
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar (S/N)? '))
    if cont in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')