nome = str(input('Nome do aluno: '))
nota1 = float(input('Nota P1: '))
nota2 = float(input('Nota P2: '))
recu = 0
media1 = (nota1 + nota2) / 2
if media1 <= 6:
    recu = float(input('Nota Recuperaçao: '))
    if nota1 >= nota2 and nota1 >= recu:
        maior = nota1
        if nota2 >= recu:
            segundamaior = nota2
            media2 = (maior + segundamaior)/2
            if media2 >= 6:
                print(media2, 'voce esta aprovado')
            else:
                print(media2, 'voce esta reprovado')
        else:
            segundamaior = recu
            media2 = (maior + segundamaior) /2
            if media2 >= 6:
                print(media2, 'voce esta aprovado')
            else:
                print(media2, 'voce esta reprovado')
    if nota2 >= recu and nota2 >= nota1:
        maior = nota2
        if recu >= nota1:
            segundamaior = recu
            media2 = (maior + segundamaior) / 2
            if media2 >= 6:
                print(media2, 'Voce esta aprovada')
            else:
                print(media2, 'voce esta reprovada')
        else:
            segundamaior = nota1
            media2 = (maior + segundamaior) / 2
            if media2 >= 6:
                print(media2, 'Voce esta aprovada')
            else:
                print(media2, 'voce esta reprovada')
    elif recu >= nota1 and recu >= nota2:
        maior = recu
        if nota1 >= nota2:
            segundamaior = nota1
            media2 = (maior + segundamaior)/2
            if media2 >= 6:
                print(media2, 'voce esta aprovada')
            else:
                print(media2, 'voce esta reprovada')
        else:
            segundamaior = nota2
            media2 = (maior + segundamaior)/2
            if media2 >= 6:
                print(media2, 'voce esta aprovada')
            else:
                print('voce esta reprovada')
else:
    print(media1, 'Voce esta APROVADO!')
