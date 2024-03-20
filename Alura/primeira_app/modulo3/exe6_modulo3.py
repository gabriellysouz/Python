#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista = [2,6,4,'2',10,5,0]
soma = 0

try:
    for n in lista:
        soma+=n
    print(soma)
except:
    print('Existe algum dado invalido, verifique novamente')

