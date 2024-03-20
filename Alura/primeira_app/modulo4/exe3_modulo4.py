#Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.


num_quadrado = {}

for n in range (1,6):
    q = n*n
    num_quadrado[f'{n}²'] = q

print(num_quadrado)