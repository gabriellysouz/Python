sal = float(input('Qual o salario do funcionario? R$'))
if sal > 1250.00:
    novo = (sal/100) * 10
    n1 = sal + novo
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(sal, n1))
if sal <= 1250.00:
    cor = (sal/100) * 15
    n2 = sal + cor
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(sal, n2))
print('Bom trabalho!')
