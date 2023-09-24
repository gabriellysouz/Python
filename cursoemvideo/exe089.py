#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
#notas de cada aluno individualmente.

boletim = []
nome = []
cont = 'Ss'
while cont not in 'Nn':
    nome1 = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media1 = (nota1 + nota2) / 2
    boletim.append([nome1, nota1, nota2, media1])
    cont = str(input('Quer continuar (S/N)? '))
print('-' * 30)
print('{:<5}'.format('Nº'), end='')
print('{:<15}'.format('Nome'), end='')
print('{:<5}'.format('Media'))
print('-' * 30)

for posicao, aluno in enumerate(boletim):
    nome = aluno[0]
    media = aluno[3]
    print('{:<5}'.format(posicao), end='')
    print('{:<15}'.format(nome), end='')
    print('{:<5}'.format(media))
print('-' * 30)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if mostrar == 999:
        break
    else:
        print(f'notas de {boletim[mostrar][0]} sao {boletim[mostrar][1:3]}')
    print('-' * 30)
