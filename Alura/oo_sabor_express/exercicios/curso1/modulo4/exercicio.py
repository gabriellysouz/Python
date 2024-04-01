#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        Livro.livros.append(self)

 #Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro.   
    def __str__(self):
        return f'Titutlo: {self.titulo} | Autor: {self.autor} | Ano: {self.ano} |{self.status} '
 
 #Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.    
    @property
    def status(self):
        return 'Disponivel' if self.disponivel else 'Indisponivel'

    def emprestar(self):
        self.disponivel = not self.disponivel

#Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        aux = False
        for l in Livro.livros:
            if l.ano == ano and l.disponivel:
                print(f'Titutlo: {l.titulo} | Autor: {l.autor}')
                aux = True
        if aux == False:
            print('Nenhum livro encontrado')
    
    
#Crie duas instâncias da classe Livro e imprima essas instâncias.
#livro1= Livro('Dom Casmurro', 'Machado de Assis', 1899)
#livro2 = Livro('Caçador de Pipas', 'Khaled Hosseini', 2003 )

#Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
#livro1.emprestar()

#print(livro1)
#print(livro2)

#Livro.verificar_disponibilidade(2005)
