from random import randint
cont = 0
while True:
    compu = randint(1, 10)
    usuario = int(input('Digite um numero: '))
    parimpar = str(input('Par ou Impar? (P/I) ')).strip().upper()[0]
    print('-' * 20)
    resul = compu + usuario
    print(f'O computador jogou {compu} e voce jogou {usuario}. Total de {resul} deu ', end='')
    print('PAR' if resul % 2 == 0 else 'IMPAR')
    if parimpar == 'P' and resul % 2 == 0:
        print('Voce VENCEU!')
        cont += 1
    elif parimpar == 'P' and resul % 2 == 1:
        break
    elif parimpar == 'I' and resul % 2 == 1:
        print('Voce VENCEU!')
        cont += 1
    elif parimpar == 'I' and resul % 2 == 0:
        break
    print('-' * 20)
    print('Vamos jogar novamente... ')
print('-' * 20)
print('VOCE PERDEU!')
print(f'GAME OVER... Voce venceu {cont} vezes')

