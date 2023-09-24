#Crie um programa que tenha a função leiaInt(), que vai
# funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor
# numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(texto):
    ok = False
    valor = 0
    while True:
        n = str(input(texto))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um numero inteiro valido')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Voce digitou o numero {n}')


