#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preço=float(input('Digite o preço do produto_'))
descon=preço*0.05
print(f'De R${preço} você vai pagar R${preço-descon}! Parabéns você ganhou 5% de desconto.')