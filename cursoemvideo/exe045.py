from random import randint
from time import sleep
compu = randint(0,2)
print('Suas opçoes: \n[0] PEDRA \n[1] PAPEL \n[2] TESOURA')
esc = int(input('Qual é sua jogada? '))
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!!')
sleep(1)
print('-=-' * 10)
if esc < 0 or esc > 2:
    print('Resposta Invalida')
elif compu == 0:
    print('Computador jogou PEDRA')
    if esc == 0:
        print('Jogador jogou PEDRA')
        print('-=-' * 10, '\nEMPATOU')
    elif esc == 1:
        print('Jogador jogou PAPEL')
        print('-=-'*10 ,'\nJOGADOR VENCE')
    elif esc == 2:
        print('Jogador joogu TESOURA')
        print('-=-'*10 ,'\nCOMPUTADOR VENCE')
elif compu == 1:
    print('Computador jogou PAPEL')
    if esc == 1:
        print('Jogador jogou PAPEL')
        print('-=-' * 10, '\nEMPATOU')
    elif esc == 0:
        print('Jogador jogou PEDRA')
        print('-=-'*10 ,'\nCOMPUTADOR VENCE')
    elif esc == 2:
        print('Jogador jogou TESOURA')
        print('-=-'*10 ,'\nJOGADOR VENCE')
elif compu == 2:
    print('Computador jogou TESOURA')
    if esc == 2:
        print('Jogador jogou TESOURA')
        print('-=-' * 10, '\nEMPATOU')
    elif esc == 0:
        print('Jogador jogou PEDRA')
        print('-=-'*10 ,'\nJOGADOR VENCE')
    elif esc == 1:
        print('Jogador jogou PAPEL')
        print('-=-'*10 ,'\nCOMPUTADOR VENCE')
