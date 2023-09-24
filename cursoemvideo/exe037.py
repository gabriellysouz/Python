#Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro:'))
print('Escolha uma das bases para conversao:')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opçao: '))
if escolha == 1:
    print('{} convertido parra BINARIO é {}'.format(num, format(num,'b')))
elif escolha == 2:
    print('{} convertido em OCTAL é {}'.format(num, format(num, 'o')))
elif escolha == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num, format(num, 'x')))
else:
    print('Opçao invalida')
