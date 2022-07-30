#crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#Considere US$1= R$3,27
d=float(input('Quantos reais vc tem na sua carteira?_ '))
dol=d/3.27
print(f' você consegue comprar U${dol:.3f} ')
