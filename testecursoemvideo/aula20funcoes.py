'''def titulo(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
titulo('Curso em Video ')
titulo('Legal')

def soma(a, b):
    s = a + b
    print(s)
soma(4, 5)   #entre parenteses sao os parametros
soma(8, 9)
soma(2, 1)

def soma (a, b):
    s = a + b
    print(f'A é igual a {a} e B igual {b}')
    print(f'A soma é {s}')
soma(3, 4)
soma(5, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# empacotar parametros (funcionalidade do python)
def contador(*num):
    for valor in num:
        print(valor, end=' ')
    print('Fim')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(3, 4)
soma(2, 9, 4)



