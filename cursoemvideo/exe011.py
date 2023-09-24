a = float(input('Em metros, qual a altura da sua parede? '))
l = float(input('Em metros, qual a largura da sua parede? '))
ar = a * l
lt = (a*l)/2
print('A area da sua parede é igual a {}m² e, \nconsiderando que cada litro pinta 2m², voce ira precisar de {}l de tinta.'.format(ar,lt))
