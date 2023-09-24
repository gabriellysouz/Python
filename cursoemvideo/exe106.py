#Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.

from time import sleep
def ajuda(msg):
    return help(msg)

def titulo(msg):
    print('-' * (len(msg) + 4))
    print(f'{msg}')
    print('-' * (len(msg) + 4))
    sleep(0.5)


while True:
    titulo('Sistema de Ajuda PyHelp')
    n = str(input('Funçao ou Biblioteca: '))
    if n == 'fim':
        titulo('Ate Logo')
        break
    else:
        titulo(f'Acessando o manual do comando "{n}"')
        ajuda(n)
        sleep(2)

