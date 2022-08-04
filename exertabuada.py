#Crie um programa de tabuada em que o usuario diga qual numero da tabuada ele quer saber
#em qual número essa tabuada começa e em qual termina
#use número 6 pra tabuada
#começa por 4
#termina em 8
#e se numero que começa for menor que o número que termina mostre uma msg

    #6x4=24
    #6X5=30
    #6X6=36
    #6X7=42
    #6X8=48

tabuada=int(input('Qual tabuada vc quer saber? '))
ni=int(input('Numero que inicia: '))
nf=int(input('Numero final: '))
for i in range(ni,nf+1):
    if nf<ni:
        print('Número final maior do que número inicial!')
    else:
        print(f'{tabuada}x{i}={tabuada*i}')

