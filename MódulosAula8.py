#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos 
# import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar 
# vários recursos adicionais nos seus programas utilizando módulos built-in e 
# módulos externos, oferecidos no Pypi.
from math import sqrt
num=int(input('Digite um número: '))
raiz= sqrt(num)
print(f'A Raiz quadrada de {num} é {raiz:.1f} ')