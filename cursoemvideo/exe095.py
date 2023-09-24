time = list()
jogador = dict()
golista = list()
totalgol = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou ? '))
    for p in range(1, partidas+1):
        gol = int(input(f'  Quantos gols na partida {p}? '))
        totalgol += gol
        golista.append(gol)
    jogador['gols'] = golista[:]
    jogador['total'] = totalgol
    time.append(jogador.copy())
    jogador.clear()
    golista.clear()
    totalgol = 0
    while True:
        continuar = str(input('Quer continuar (S/N)? ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')
    if continuar in 'N':
        break

print('-=' * 30)
print('{:<10}'.format('Cod'), end='')
print('{:<20}'.format('Nome'), end='')
print('{:<20}'.format('Gols'), end='')
print('{:<10}'.format('Total'))
print('-' * 60)
for j in time:
    print('{:<10}'.format(time.index(j)), end='')
    print('{:<20}'.format(j["nome"]), end= '')
    print(j['gols'], end='')
    print('{:>10}'.format(j['total']))
print('-' * 60)

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print('ERRO')
    else:
        print(f' -- Levantamendo do Jogador {time[mostrar]["nome"]} --')
        for i, g in enumerate(time[mostrar]['gols']):
            print(f'   Na partida {i+1} fez {g} gols')
        print()
