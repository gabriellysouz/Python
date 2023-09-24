'''frase = str(input('Digite uma frase: '))
semespaco = frase.replace(' ', '')
invert = semespaco[::-1]
print(semespaco)
print(invert)
if invert == semespaco:
    print('polindromo')
else:
    print('nao polindromo')'''

frase = str(input('Digite uma frase: '))
semespaco = frase.replace(' ', '')
numeroLetras = len(semespaco)

negativo = -1
palindromo = True
quantidadeLetras = (len(semespaco) - 1)

for posicao in range(1, len(semespaco)):
    if semespaco[posicao].upper() != semespaco[quantidadeLetras - posicao].upper():
        palindromo = False
    negativo -= 1

if True:
    numero = 2

print('numero: ' + str(numero))

'''for letra in semespaco:
    if letra != semespaco[negativo]:
        palindromo = False
    negativo -= 1'''

if palindromo:
    print('É palindromo')
else:
    print('Não é palindromo')