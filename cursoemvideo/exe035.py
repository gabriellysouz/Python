a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if ((b - c) < a < b + c) and ((a - c) < b < a + c) and ((a - b) < c < a + b):
    print('Os valores digitados PODEM formar um triagulo')
else:
    print('Os valores digitados NAO PODEM formar um triangulo')
