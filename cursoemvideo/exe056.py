# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
femenor = 0
velho = 0
nome1 = ''
for p in range(1, 5):
    print('='*5,'{}º PESSOA'.format(p), '='*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma = soma + idade
    if sexo in 'Ff' and idade < 20:
            femenor = femenor + 1
    elif sexo in 'Mm' and idade > velho:
        velho = idade
        nome1 = nome
media = soma / 4
print('A media de idade do grupo é de {} anos'.format(media))
print('Ao todo sao {} mulher com menos de 20 anos'.format(femenor))
print('O homem mais velho tem {} e se chama {}'.format(velho, nome1))
