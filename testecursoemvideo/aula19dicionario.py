'''pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys()) #nome, sexo, idade
print(pessoas.values()) #gustavo, M, 22

for k in pessoas.keys():
    print(k)

for k,v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'leandro' # substitui
pessoas['peso'] = 98.5 #adiciona valor na lista.


estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    estado.clear()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


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
for o in sorted(jogadores, key= jogadores.get, reverse=True): #organiza em ordem descrecente (se tirar
                                                                #se tirar o reverse=True deixa em prdem crescente
    print(o, 'com', jogadores[o], end=' ')
    print()
    sleep(1)'''