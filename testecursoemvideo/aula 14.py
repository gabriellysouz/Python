#while - repetiçao sem limite pre definido
#continua a validar ate a condiçao ser verdadeira ou falsa
#sabendo o limite pode-se escolher entre for e while. quando limite é desconhecido, usa while
'''n = 1
while n != 0:
    n = int(input('digite um valor:'))
print('fim')'''

'''r = 's'
while r == 's':
    n = int(input('digite um valor:'))
    r = str(input('quer continuar? (s/n)'))
print('fim')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('digite um valor:'))
    if n != 0:
        if n%2 == 0:
            par += 1
        else:
            impar += 1
print('impar {} par {} '.format(impar,par))
print('fim')