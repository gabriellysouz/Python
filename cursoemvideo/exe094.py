#Crie um programa que leia nome, sexo e idade de várias
# pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

totalpessoas = list()
pessoa = dict()
somaidade = 0
mulher = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo (M/F): ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F!')
    if pessoa['sexo'] in 'Ff':
        mulher += 1
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    totalpessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input('Quer continuar (S/N)?')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')
    if continuar in 'N':
        break
print('-=' * 30)
mediaidade = somaidade/len(totalpessoas)
print(f'A) Ao todo temos {len(totalpessoas)} pessoas cadastradas.')
print(f'B) A media de idade é {mediaidade:.2f} anos.')
if mulher != 0:
    print('C) As mulheres cadastradas foram ', end='')
    for listatotal in totalpessoas:
        for pess in listatotal.values():
            if pess == 'F' or pess == 'f':
                print(listatotal["nome"], end=' ')
else:
    print('C) Nao temos mulheres cadastradas.')
print()
print('D) Lista de pessoas que ficam acima da media de idade: ')
for i, v in enumerate(totalpessoas):
    if v['idade'] > mediaidade:
        print(f'    {v["nome"]} com {v["idade"]}')
