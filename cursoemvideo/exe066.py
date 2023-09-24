#Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = cont = 0
flag = 999
while True:
    num = int(input('Digite um valor[999 para parar]: '))
    if num == flag:
        break
    cont += 1
    soma += num

print(f'Voce digitou {cont} numeros e a soma entre eles é de {soma}')
