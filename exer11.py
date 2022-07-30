#faça um programa que leia a largura e a altura de uma parede em metros. Cálcule sua área e a quantidade
#de tinta necessária para pinta-la, sabendo que cada lata de tinta pinta 2m².

#teste com  |2,5 x 1.75 |     RESULTADOS= 4.375²   (2.1875L)

alt=float(input('Qual a altura de sua parede?_'))
lar=float(input('Qual a largura de sua parede?_'))
total= alt*lar
litro=total/2
print(f'{alt}x{lar}={total}m², você precisa de {litro} Litros de tinta para pintar sua parede!')
