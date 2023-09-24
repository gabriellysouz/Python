c = str(input('Em que cidade voce nasceu? ')).strip()
#s = 'santo' in c  (problema - nao reconhece maiusculas desse jeito)
print(c[:5].upper() == 'SANTO')

