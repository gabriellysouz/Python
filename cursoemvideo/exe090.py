aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] < 5:
    aluno['situaçao'] = 'Reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'Recuperaçao'
else:
    aluno['situaçao'] = 'Aprovado'
print(f'O aluno {aluno["nome"]} tem a media {aluno["media"]}')
print(aluno['situaçao'])
