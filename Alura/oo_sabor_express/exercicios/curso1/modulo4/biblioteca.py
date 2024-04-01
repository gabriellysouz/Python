#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from exercicio import Livro

#No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro1= Livro('Dom Casmurro', 'Machado de Assis', 1899)
livro2 = Livro('Caçador de Pipas', 'Khaled Hosseini', 2003 )
livro3 = Livro('Precisamos falar sobre kevin', 'Lionel Shriver', 2003)
livro4 = Livro('Harry Potter e a Ordem da Fênix', 'J. K. Rowling', 2003)


livro1.emprestar()

#No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

Livro.verificar_disponibilidade(2005)

