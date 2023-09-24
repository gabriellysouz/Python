nome = str(input('qual seu nome: '))
if nome == 'gustavo':
    print('que nome bonito')
elif nome == 'pedro' or nome == 'maria' or nome == 'joao':
    print('seu nome é comum no brasil')
elif nome in 'ana claudia julia':
    print('belo nome feminino')
else:
    print('seu nome é normal')
print('tenha um bom dia {}'.format(nome))
