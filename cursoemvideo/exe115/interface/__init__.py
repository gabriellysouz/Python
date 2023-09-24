#menu

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


def linha(tam=40):
    return '-' * tam


def cabecalho(texto):
    print(linha())
    print(f'{texto}'.center(40))
    print(linha())
def menu(lista, opçao=0):
    cabecalho('Menu Principal')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}')
        cont += 1
    print(linha())
    op = leiainteiro('Sua opçao: ')
    return op
