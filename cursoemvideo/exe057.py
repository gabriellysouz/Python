#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input('Informe seu sexo (m/f): ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dado invalido. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))
