from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-' * 20, '\nVou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
usu = int(input('Em que numero eu pensei? '))
print('Processando..')
sleep(2)
if usu == comp:
    print('Parabens! Voce conseguiu me vencer!')
if usu != comp:
    print('Tente novamente..')
    us = int(input('Em que numero eu pensei? '))
    if usu == comp:
        print('Parabens! Voce conseguiu me vencer!')
    else:
        print('Ganhei! Eu pensei no numero {} e nao no {}'.format(comp, usu))
