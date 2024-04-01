class musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = musica()
musica1.nome = 'Sweet Home Alabama'
musica1.artista = 'Lynyrd Skynyrd'
musica1.duracao = 285

musica2 = musica()
musica2.nome = 'Start Me Up'
musica2.artista = 'The Rolling Stones'
musica2.duracao = 214

musica3 = musica()
musica3.nome = 'Bohemian Rhapsody'
musica3.artista = 'Queen'
musica3.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
print(f'Música: {musica2.nome} - Banda: {musica2.artista} - {musica2.duracao} segundos')
print(f'Música: {musica3.nome} - Banda: {musica3.artista} - {musica3.duracao} segundos')

