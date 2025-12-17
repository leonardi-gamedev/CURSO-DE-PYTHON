#Dados Altura e largura de uma parede, calcular a quantidade de tinta para pintar 1L=2m2
altura= float(input('Qual a altura de parede que será pintada? '))
largura= float(input('E sua largura? '))
area = altura * largura
quant = area / 2
print(f'Considerando que cada litro de tinta pinta dois metros quadrados da parede\n'
      f'será necessário {quant:.2f} Litros de tinta.')