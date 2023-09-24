#Crie um programa que leia nome, ano de nascimento e carteira
# de trabalho e cadastre-o (com idade) em um dicionário. Se
# por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
anoatual = date.today().year
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = anoatual - anonasc
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 nao tem): '))

if trabalhador['CTPS'] != 0:
    contrato = int(input('Ano de Contrataçao: '))
    trabalhador['Salario'] = float(input('Salario: R$'))
    trabalhador['Aposentadoria'] = contrato + 35
    print('-=' * 20 )
    for k, v in trabalhador.items():
        if trabalhador['Aposentadoria'] > anoatual:
            print('- ', k, 'tem o valor', v, end=' ')
            print()
        else:
            print('- ', k, 'tem o valor', v, end=' ')
            print()
    if trabalhador['Aposentadoria'] < anoatual:
        print('- Voce ja deveria ter se aposentado')
else:
    print('-=' * 20 )
    for k, v in trabalhador.items():
        print('- ', k, 'tem o valor', v, end=' ')
        print()


