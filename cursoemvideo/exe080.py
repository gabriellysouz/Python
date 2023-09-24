#Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o
# sort()). No final, mostre a lista ordenada na tela.

#resoluçao com ajuda do Lu
lista = []
for l in range(0, 5):
    valor = int(input('Digite um valor: '))
    adicionouNaLista = False
    for i, v in enumerate(lista):
        if valor < v:
            adicionouNaLista = True
            lista.insert(i, valor)
            print(f'adicionado na posição {i}')
            break
    if adicionouNaLista == False:
        lista.append(valor)
        print('adicionado no fim da lista')
print(f'lista na ordem {lista}')

#resoluçao guanabara
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n<= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posiçao {pos} da lista...')
                break
            pos += 1
print(f'os valores em ordem sao {lista}')
