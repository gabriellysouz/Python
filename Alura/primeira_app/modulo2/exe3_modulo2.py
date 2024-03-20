#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario = 'natinha'
senha = 'natinha123'

inserir_usu = input('Insira o usuario: ')
inserir_senha = input('Insira a senha: ')

if inserir_usu == usuario and inserir_senha == senha:
    print('Acesso permitido')
else:
    print('Acesso negado')
