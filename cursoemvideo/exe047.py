#Crie um programa que mostre na tela todos os números pares que
# estão no intervalo entre 1 e 50.
'''for par in range(1, 51):
    if par % 2 == 0:
        print(par, end=' ')
print('Acabou')'''

# soluçao guanabara (mais eficiente)
for par in range(2, 51, 2):
    print(par, end=' ')
print('Acabou')
