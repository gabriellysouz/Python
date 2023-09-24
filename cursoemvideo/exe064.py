#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

soma= 0
flag = 999
num = 0
count = -1
while num != flag:
    num = int(input('Digite um numero [999 para parar]: '))
    soma = soma + num
    count += 1
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(count, soma - flag))
