# Crie um programa que tenha uma função fatorial() que
# receba dois parâmetros: o primeiro que indique o
# número a calcular e outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.
'''def fatorial(num):
    fat = 1
    for n in range(num, 0, -1):
        fat = fat * n
    return fat

def mostrar():
    if aparecer in 'Ss':
        fat = 1
        for n in range(num, 1, -1):
            fat = fat * n
            print(f'{n} x ', end='')
        print(f'1 =', end=' ')
        return fat
    else:
        return 'Volte sempre'


num = int(input('Digite um numero para ver o fatorial: '))
print(fatorial(num))
aparecer = str(input('Gostaria de ver o calculo? '))
print(mostrar())'''

def fatorial(num, show=False):
    fat = 1
    for n in range(num, 1, -1):
        fat = fat * n
        if show:
            print(f'{n} x ', end='')
            if n == 2:
                print(f'1 =', end=' ')
    return fat

print(fatorial(5, show=False))
