from interface import *
from arquivo import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerarquivo('pessoas.txt')
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiainteiro('Idade: ')
        cadastrar('pessoas.txt', nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do programa... Ate logo')
        break
    else:
        cabecalho('ERRO! Por favor digite um numero inteiro valido')
    sleep(2)
