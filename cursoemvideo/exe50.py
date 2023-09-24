#Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for p in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voce digitou {} numeros pares e a soma entre eles é {}'.format(cont, soma))

