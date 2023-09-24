from datetime import date
ano = int(input('Pressione 0 para analisar o ano atual ou digite outro qualquer: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é bissexto'.format(ano))
        else:
            print('O ano {} não é bissexto'.format(ano))
    else:
        print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} nao é bissexto'.format(ano))

