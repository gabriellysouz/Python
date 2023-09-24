#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('Por favor indique o sexo: \n[1] mulher \n[2] homem')
sex = int(input('Opçao escolhida: '))
if sex == 1:
    print('Voce nao precisa se alistar')
elif sex == 2:
    nasc = int(input('Ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    minimo = 18
    falta = minimo - idade
    quando = nasc + minimo
    deveria = ano - quando
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))
    if idade < minimo:
        print('Ainda falta {} anos para se alistar'.format(falta))
        print('Seu alistamento sera em {}'.format(quando))
    elif idade == minimo:
        print('Voce deve se alistar IMEDIATAMENTE')
    else:
        print('Voce deveria ter se alistado ha {} anos'.format(deveria))
        print('Seu alistamento foi em {}'.format(quando))
else:
    print('Opçao invalida')