
class Musica:
    
    list_musica = []
    
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.list_musica.append(self)

    def exibir_musicas():
        for musica in Musica.list_musica:
            print(f'Nome: {musica.nome} | Artista: {musica.artista} | Duraçao: {musica.duracao} seg')
            print()




musica1 = Musica('Sweet Home Alabama', 'Lynyrd Skynyrd', 285)
musica2 = Musica('Start Me Up', 'The Rolling Stones', 214 )
musica3 = Musica('Bohemian Rhapsody', 'Queen', 355 )

Musica.exibir_musicas()
