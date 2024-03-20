import os

restaurantes = [{'nome':'Hon Kong', 'categoria':'Japonesa', 'status':False},
                {'nome':'TelePizza', 'categoria':'Pizza', 'status':True},
                {'nome':'Brasaria', 'categoria':'Portuguesa', 'status':False}]

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def limpar_titulo(txt):
    os.system('cls')
    print(txt)
    print('  ')

def finalizar_app():
    limpar_titulo('Finalizando...')

def opcao_invalida():
    print('Opçao invalida')
    voltar_menu()

def exibir_opcoes():
    ''' Essa funçao é responsavel por listar as opçoes do menu '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar status do Restaurante')
    print('4. Sair \n')

def cadastrar_restaurante():
    ''' Essa funçao é responsavel por cadastrar um novo restaurante'''
    limpar_titulo('Cadastro novo restaurante')
    nome_rest = input('Digite o nome do restaurante que deseja cadastrar: ')
    categ_rest = input(f'Digite a categoria do restaurante {nome_rest}: ')
    dados_rest = {'nome': nome_rest, 'categoria':categ_rest, 'status':False}
    restaurantes.append(dados_rest)
    print(f'\nO restaurante {nome_rest} foi cadastrado com sucesso!\n')
    voltar_menu()

def listar_rest():
    ''' Essa funçao é responsavel por listar todos os restaurante cadastrados'''
    limpar_titulo('Lista de Restaurantes Cadastrados:')
    for item in restaurantes:
        ativo = 'ativado' if item['status'] else 'desativado'
        print(f"-{item['nome'].ljust(20)} {item['categoria'].ljust(20)} {ativo}")
    voltar_menu()

def alternar_status_rest():
    ''' Essa funçao é responsavel por alterar o status dos restaurantes cadastrados para ativo ou desativo'''
    limpar_titulo('Alternando o status do restaurante')
    nome_rest = input('Digite o nome do restaurante que deseja alternar o status: ')
    rest_encontrado= False
    for res in restaurantes:
        if nome_rest == res['nome']:
            rest_encontrado = True
            res['status'] = not res['status']
            msg = f'O restaurante {nome_rest} foi ativado com sucesso' if res['status'] else f'O restaurante {nome_rest} foi desativado com sucesso'

            print(msg)
    if not rest_encontrado:
        print('Restaurante nao encontrado')
    voltar_menu()

def escolher_opcao():
    ''' Essa funçao é responsavel validar a opçao do menu e responder de acordo '''
    try:
        opcao_escolhida = int(input('Escolha uma opçao: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_rest()
        elif opcao_escolhida == 3:
            alternar_status_rest()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_titulo('Sabor Express')
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


