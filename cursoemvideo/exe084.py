#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas.    B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

nomepeso = []
dados = []
maiorpeso = []
menorpeso = []
contador = 0

cont = 'Ss'
while cont not in 'Nn':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso kg: ')))
    nomepeso.append(dados[:])
    contador += 1
    if contador == 1:
        maiorpeso.append(dados[1])
        maiorpeso.append(dados[0])
        menorpeso.append(dados[1])
        menorpeso.append(dados[0])
    else:
        if dados[1] >= maiorpeso[0]:
            if dados[1] == maiorpeso[0]:
                maiorpeso.append(dados[0])
            if dados[1] > maiorpeso[0]:
                maiorpeso.clear()
                maiorpeso.append(dados[1])
                maiorpeso.append(dados[0])
        elif dados[1] <= menorpeso[0]:
            if dados[1] == menorpeso[0]:
                menorpeso.append(dados[0])
            if dados[1] < menorpeso[0]:
                menorpeso.clear()
                menorpeso.append(dados[1])
                menorpeso.append(dados[0])
    dados.clear()
    cont = str(input('Deseja continuar (S/N): '))
print('-=' * 30)
print(f'Foram cadastradas {contador} pessoas')
print(f'O maior peso foi de {maiorpeso[0]}Kg. Peso de {maiorpeso[1:]}')
print(f'O maior peso foi de {menorpeso[0]}Kg. Peso de {menorpeso[1:]}')

#resoluçao guanabara
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men == temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo voce cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
