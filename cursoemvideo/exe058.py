#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint
comp = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um numero de 0 a 10. \nSera que voce consegue adivinhar?')
usuario = int(input('Qual o seu palpite? '))
cont = 1

while usuario != comp:
    cont += 1
    if usuario > comp:
        print('Menos... Tente mais uma vez ')
    else:
        print('Mais... Tente novamente')
    usuario = int(input('Qual seu palpite? '))
print('Acertou com {} tentativas. Parabens!'.format(cont))
