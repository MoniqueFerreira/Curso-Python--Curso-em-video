# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que 
# o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('Qual a quantidade de km foi percorrida? _'))
dia=float(input('Quantos dias você ficou com o carro? _'))
v1=dia*60
v2=km*0.15
print(f'você gastou R${v1} pelos dias que ficou com o carro e R${v2} pelos km rodados o total do aluguel é R${v1+v2}')