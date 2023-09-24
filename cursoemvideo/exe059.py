#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar   [ 2 ] multiplicar
# [ 3 ] maior   [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
print('-' * 10)
opcao = 0
historico = ''
while opcao != 8:
    sleep(1)
    print('[1] SOMAR \n[2] MULTIPLICAR \n[3] SUBTRAIR \n[4] DIVIDIR \n[5] MAIOR '
          '\n[6] NOVOS NUMEROS \n[7] HISTORICO \n[8] SAIR')
    opcao = int(input('>>> Qual sua opção? '))
    if opcao > 8 or opcao < 1:
        print('Opção invalida. Digite novamente.')
    else:
        if opcao == 1:
            soma = num1 + num2
            textoSoma = 'A soma entre {} e {} é {}'.format(num1, num2, soma)
            historico += textoSoma + '\n'
            print(textoSoma)
        elif opcao == 2:
            multi = num1 * num2
            textoMultiplicacao = 'O resultado de {} x {} é {}'.format(num1, num2, multi)
            historico += textoMultiplicacao + '\n'
            print(textoMultiplicacao)
        elif opcao == 3:
            menos = num1 - num2
            textoSubtraco = 'O resultado da subtração entre {} e {} é {}'.format(num1,num2, menos)
            historico += textoSubtraco + '\n'
            print(textoSubtraco)
        elif opcao == 4:
            if num1 == 0 or num2 ==0:
                print('O valor 0 nao é divisivel, Selecione opçao 6 no menu para alterar os valores.')
            else:
                divide = num1 / num2
                textoDivisao = 'A divisao entre {} e {} é {}'.format(num1, num2, divide)
                historico += textoDivisao
                print(textoDivisao)
        elif opcao == 5:
            if num1 > num2:
                print('Entre {} e {} o maior valor é {}'.format(num1, num2, num1))
            else:
                print('Entre {} e {} o maior valor é {}'.format(num1, num2, num2))
        elif opcao == 6:
            print('-' * 10)
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))
            historico = ''
        elif opcao == 7:
            if (historico != ''):
                print(historico)
            else:
                print('Nenhum histórico disponivel')
    print('-' * 10)
print('Fim, volte sempre!')
