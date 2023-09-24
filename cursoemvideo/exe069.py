print('-' * 20)
print('CADASTRO')
print('-' * 20)
menor20 = 0
homem = 0
maior18 = 0
while True:
    idade= int(input('Idade: '))
    sexo = '0'
    while sexo not in 'MF':
        sexo = str(input('Sexo (M/F): ')).upper().strip()[0]
    print('-' * 20)
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            menor20 += 1
    conti = '0'
    while conti not in 'SN':
        conti = str(input('Quer continuar? (S/N) ')).upper().strip()[0]
    print('-' * 20)
    if conti == 'N':
            break

print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Homens cadastrados: {homem}')
print(f'Mulheres menores de 20 anos: {menor20}')

