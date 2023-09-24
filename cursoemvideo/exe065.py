#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'Ss'
soma = 0
cont = 0
maior = 0
menor = 0
while continuar not in 'Nn':
    num = int(input('Digite um valor: '))
    soma = soma + num
    cont = cont + 1
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Voce digitou {cont} numeros e a media entre eles foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
