'''print('-' * 15)
print('{:^15}'.format('Banco'))
print('-' * 15)
while True:
    valor = int(input('Qual valor voce quer sacar? R$'))
    cinqint = valor // 50
    cinqint2 = valor - (cinqint * 50)
    vintint = cinqint2 // 20
    vintint2 = cinqint2 - (vintint * 20)
    dezint = vintint2 // 10
    dezint2 = vintint2 - (dezint *10)
    umint = dezint2 // 1
    if cinqint > 0:
        print(f'Total de {cinqint} notas de R$50')
    if vintint > 0:
        print(f'Total de {vintint} notas de R$20')
    if dezint > 0:
        print(f'Total de {dezint} notas de R$10')
    if umint > 0:
        print(f'Total de {umint} notas de R$1')
    if valor > 0:
        break
print('-' * 15)
print('Volte sempre!')'''

#soluçao lucas <3
print('-' * 15)
print('{:^15}'.format('Banco'))
print('-' * 15)
notasDisponiveis = [50, 20, 10, 1]
valor = int(input('Qual valor voce quer sacar? R$'))
for nota in notasDisponiveis:
    quantidadeNotas = valor // nota
    valor -= quantidadeNotas * nota
    if quantidadeNotas > 0:
        print(f'Total de {quantidadeNotas} notas de R${nota}')
    if valor == 0:
        break
print('-' * 15)
print('Volte sempre!')
