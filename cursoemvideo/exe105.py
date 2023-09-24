#Faça um programa que tenha uma função notas() que
# pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*num, sit=False):
    maior = menor = cont = soma = 0
    final = {}
    for n in num:
        cont += 1
        soma += n
        if cont == 1:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
    media = soma / cont
    final['Total: '] = cont
    final['Maior: '] = maior
    final['Menor: '] = menor
    final['Media: '] = media
    if sit:
        if media >= 7.5:
            final['Situaçao'] = 'Boa'

        elif media >= 5 < 7.5:
            final['Situaçao'] = 'Razoavel'
        else:
            final['Situaçao'] = 'Ruim'
    return final


n = notas(1, 5, 2, 7.5, 6, sit=True)
print(n)
