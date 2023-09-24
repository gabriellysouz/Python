from exe115 import interface

def lerarquivo(nome):
    a = open(nome, 'rt')
    interface.cabecalho('Pessoas Cadastradas')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao tentar abrir arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever no arquivo')
        else:
            print(f'Registro de {nome} adiconado')

