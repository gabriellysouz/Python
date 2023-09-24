def leiadinheiro(texto):
    while True:
        n = str(input(texto)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'ERRO! "{n}" nao é um preço valido')
        else:
            return float(n)
