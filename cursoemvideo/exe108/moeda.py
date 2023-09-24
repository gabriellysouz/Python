def aumentar(n, p):
    num = n + ((n/100) * p)
    return num

def diminuir(n, p):
    num = n - ((n/100)*p)
    return num


def dobro(n):
    num = n * 2
    return num


def metade(n):
    num = n/2
    return num

#exercicio 108
def formoeda(n):
    formatado = f'R${n:.2f}'.replace('.', ',')
    return formatado
