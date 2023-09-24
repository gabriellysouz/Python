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
