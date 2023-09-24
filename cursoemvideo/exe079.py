#Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores  = list()
cont = 'Ss'
while cont not in 'Nn':
    val = (int(input('Digite um valor: ')))
    if val in valores:
            print('Valor repetido')
    else:
        valores.append(val)
        print('Valor adicionado')
    cont = str(input('Quer continuar? '))
print('-' * 30)
valores.sort()
print(f'os valores digitados foram {valores}')

