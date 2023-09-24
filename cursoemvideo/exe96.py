# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A area de um terreno de {l:.2f} x {c:.2f} é de {a:.2f}m2')
def espaco():
    print('-' * 30)

print('Controle de Terreno')
espaco()
while True:
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    area(l, c)
    espaco()
    continuar = str(input('Validar outro terreno (S/N)? '))
    espaco()
    if continuar in 'Nn':
        break
print('Obrigada, volte sempre')
