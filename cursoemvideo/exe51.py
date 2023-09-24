#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('='*25)
print('10 TERMOS DE UMA PA')
print('='*25)
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
soma = 0
for c in range(1, 11):
    soma = primeirotermo + (c - 1) * razao
    print('{} ->'.format(soma), end=' ')
print('Acabou')
