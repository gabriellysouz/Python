#Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

print()
print('Valores Sorteados: ')
sleep(0.6)
jogadores = dict()
for jogo in range(1,5):
    dado = randint(1,6)
    jogadores[f'Jogador {jogo}'] = dado

for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.', end=' ')
    print()
    sleep(0.6)
print('-' * 30)
print('RANKING DOS JOGADORES ')
sleep(0.4)
for o in sorted(jogadores, key= jogadores.get, reverse=True):
    print(o, 'com', jogadores[o], end=' ')
    print()
    sleep(1)

