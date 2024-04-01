# Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes
# Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

from carro import Carro
from moto import Moto

carro1 = Carro('mercedes', 'SUV', 4)
moto1 = Moto('harley', 'custom', 'esportiva')

# Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

print(carro1)
print(moto1)