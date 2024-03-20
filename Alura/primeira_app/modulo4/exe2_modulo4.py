#Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

pessoa1= {'nome': 'Lucas', 'idade':31, 'cidade':'Porto'}

pessoa1['idade'] = 45
pessoa1['estado civil'] = 'casado '

print(pessoa1)

pessoa1.pop('cidade')

print(pessoa1)


