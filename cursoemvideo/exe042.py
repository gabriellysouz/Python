#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if ((b - c) < a < b + c) and ((a - c) < b < a + c) and ((a - b) < c < a + b):
    print('Os valores digitados PODEM formar um triagulo', end=' ')
    if a != b and a != c and b != c:
        print('ESCALENO')
    elif a == b and b == c and a == c:
        print('EQUILATERO')
    else:
        print('ISOCELES')
else:
    print('Os valores digitados NAO PODEM formar um triangulo')
