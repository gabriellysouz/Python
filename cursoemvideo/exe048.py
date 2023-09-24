#Faça um programa que calcule a soma entre todos os números que são múltiplos de
# três e que se encontram no intervalo de 1 até 500.
soma = 0   #acumulador
cont = 0   #contador
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma = soma + impar
        cont = cont + 1
print('A soma dos {} valores encontrados é de {}'.format(cont, soma))
