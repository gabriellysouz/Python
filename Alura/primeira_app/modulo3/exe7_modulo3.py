#Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista =[2,4,6,'a',10,36,2]
soma = 0

try:
    for n in lista:
        soma += n
    
    media = soma/len(lista)
    print(f'A soma dos elementos {lista} é igual a {soma}')
    print(f'A media dos valores é de {media:.2f}')

except:
    print('Lista vazia ou dado invalido, verifique e tente novamente ')


