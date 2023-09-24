#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Nota P1: '))
nota2 = float(input('Nota P2: '))
media = (nota1 + nota2)/2
minimor = 5
minimor2 = 6.9
minimoa = 7
if media >= minimoa:
    print('Sua media foi {}, voce esta APROVADO'.format(media))
elif media >= minimor and media < minimor2:
    print('Sua media foi {}, voce esta de RECUPERAÇAO'.format(media))
else:
    print('Sua media foi {}, voce esta REPROVADO'.format(media))