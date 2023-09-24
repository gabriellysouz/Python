expressao = str(input('Digite a expressao: '))
posicao = []
aberto = 0
fechado = 0

for e in expressao:
    if e == '(':
        posicao.append('(')
    elif e == ')':
        if len(posicao) > 0:
            posicao.pop()
        else:
            posicao.append(')')
            break
if len(posicao) == 0:
    print('expressao valida')
else:
    print('expressao invalida')




