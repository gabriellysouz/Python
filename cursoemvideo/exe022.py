nome = str(input('Digite seu nome completo: ')).strip()
l = nome.split()
t = len(nome) - nome.count(' ')
p = len(l[0])
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'. format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(t))
print('Seu primeiro nome é {} e ele tem {} letras'.format(l[0].capitalize(), p))







