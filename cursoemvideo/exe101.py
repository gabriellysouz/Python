#Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade} anos: ', end='')
    if 18 <= idade < 65:
        return 'Voto Obrigatorio'
    elif idade < 16:
        return 'Nao Vota'
    elif idade == 17 or idade > 65:
        return 'Voto Opcional'


ano = int(input('Em que ano voce nasceu? '))
print(voto(ano))
