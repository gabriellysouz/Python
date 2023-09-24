#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos = []
dados = []
print('-' * 40)
print('{:^40}'.format('JOGO NA MEGA SENA'))
print('-' * 40)
numjogos = int(input('Quantos jogos voce quer que eu sorteie? '))
print()
for j in range(0, numjogos):
    while len(dados) < 6:
        sorteio = randint(1, 60)
        if sorteio not in dados:
            dados.append(sorteio)
    dados.sort()
    jogos.append(dados[:])
    dados.clear()
sleep(0.5)
for lista in jogos:
    print('Jogo {:>2}: {} '.format(jogos.index(lista)+1, lista), end='')
    sleep(1)
    print()
print()
print('{:^30}'.format('BOA SORTE'))


