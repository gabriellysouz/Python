def aumentar(n=0, p=0, f=False):
    num = n + ((n/100) * p)
    if f:
        formatado = f'R${num:.2f}'.replace('.', ',')
        return formatado
    return num

def diminuir(n=0, p=0, f=False):
    num = n - ((n/100)*p)
    if f:
        formatado = f'R${num:.2f}'.replace('.', ',')
        return formatado
    return num


def dobro(n=0, f=False):
    num = n * 2
    if f:
        formatado = f'R${num:.2f}'.replace('.', ',')
        return formatado
    return num


def metade(n=0, f=False):
    num = n/2
    if f:
        formatado = f'R${num:.2f}'.replace('.', ',')
        return formatado
    return num

#exercicio 108
def formoeda(n):
    formatado = f'R${n:.2f}'.replace('.', ',')
    return formatado


def resumo(n=0, pa=10, pd=5):
    print('-' * 30)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 30)
    print(f'Preço analisado:\t{formoeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço:\t{metade(n, True)}')
    print(f'Com {pa}% de aumento:\t{aumentar(n, pa, True)}')
    print(f'Com {pd}% de reduçao:\t{diminuir(n, pd, True)}')
    print('-' * 30)