'''num = [2, 5, 9, 1]
num[2] = 3   #substitui a posição 2
num.append(7)  #adicionou o numero 7 no fim da lista
num.sort(reverse=True)  #sort() ordem crescente, reverse=True ordem descrescente
num.insert(2,2)  #na posiçao 2 inserir valor 0.
#num.pop()   #elimina o ultimo valor
#num.pop(2)  #elimina elemento da posição 2
num.remove(2)  #remove o valor. elimina a primeira ocorrencia do valor indicado
if 4 in num:
    num.remove(4)
else:
    print('nao achei o numero 4')
print(num)
print(f'essa lista tem {len(num)} elementos')  #tamanho da lista'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'na posiçao {c} encontrei o valor {v}')
print('cheguei ao final da lista ')'''

'''valores = list()
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)'''

'''a = [2, 3, 4, 7]
b = a     #faz ligação entre uma lista e outra, se alterar valor de uma lista, altera tambem na outra
print(f'lista a {a}')
print(f'lista b {b}')'''

a = [2, 3, 4, 7]
b = a[:]   #copia dos valores, dessa forma nao tem ligação
b[2] = 8   #agora somente a lista b recebe a alteraçao
print(f'lista a {a}')
print(f'lista b {b}')

