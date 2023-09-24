'''pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])'''

'''pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

'''pessoas = []
dados = []
maior = menor = 0
for c in range(0,3):
    dados.append(str(input('nome: ')))
    dados.append(int(input('idade: ')))  #[:] copia os dados
    pessoas.append(dados[:])  # [
    dados.clear()
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'temos {maior} maiores e {menor} menores de idade')'''



lista = [['maria', [6,8,7.5]], ['joao', [6,8,7.5]]]
print(lista[0])
print(lista[0][0])
print(lista[0].index('7.5'))

