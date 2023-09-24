def leiainteiro(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print('Erro! Digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida')
            return 0
        else:
            return n


def leiafloat(texto):
    while True:
        try:
            n = float(input(texto))
        except (ValueError, TypeError):
            print('Erro! Digite um numero real valido')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida')
            return 0
        else:
            return n
