#importando a biblioteca random

#import random
#num = random.randint(1,10)  #isso faz com que o computador te dê um número aleatório ao invés de por input para o usuário
#print(num)


#criei um programa pra simular um sorteio, a pessoa coloca o número que se inicia 
# até o ultimo numero. e o programa escolhe 1 numero entre esses aleatóriamente
import random
n1=int(input('Número inicial: '))
n2=int(input('Número final: '))
num= random.randint(n1,n2)
print(num)
