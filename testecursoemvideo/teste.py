mediaLimite = 7
nome = str(input('Nome do aluno: '))
nota1 = float(input('Nota P1: '))
nota2 = float(input('Nota P2: '))
recu = 0
maior = 0
segundamaior = 0
media1 = (nota1 + nota2) / 2
if media1 <= mediaLimite:
    recu = float(input('Nota Recuperaçao: '))
    if nota1 >= nota2:
        if nota2 >= recu:
            maior = nota1
            segundamaior = nota2
        elif recu >= nota1:
            maior = recu
            segundamaior = nota1
        else:
            maior = nota1
            segundamaior = recu
    else:
        if nota1 >= recu:
            maior = nota2
            segundamaior = nota1
        elif recu >= nota2:
            maior = recu
            segundamaior = nota2
        else:
            maior = nota2
            segundamaior = recu
    media2 = (maior + segundamaior) / 2
    if media2 >= mediaLimite:
        print(media2, 'voce esta aprovado')
    else:
        print(media2, 'voce esta reprovado')
else:
    print(media1, 'Voce esta APROVADO!')
