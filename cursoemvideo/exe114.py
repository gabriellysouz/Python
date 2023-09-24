#O site esta acessivel?

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim nao esta disponivel no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')