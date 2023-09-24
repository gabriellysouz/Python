#Crie um programa que gerencie o aproveitamento de
# um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai
# ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

dadosjogador = dict()
dadosjogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dadosjogador["Nome"]} jogou? '))
golista = []
totalgols = 0
for p in range(1, partidas+1):
    gols = (int(input(f'    Quantos gols na partida {p}? ')))
    totalgols += gols
    golista.append(gols)
dadosjogador['gols'] = golista[:]
dadosjogador['total'] = totalgols
print('-=' * 30)
print(dadosjogador)
print('-=' * 30)
for k, v in dadosjogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {dadosjogador["Nome"]} jogou {partidas}')
for i, g in enumerate(golista):
    print(f'  => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {totalgols} gols')
