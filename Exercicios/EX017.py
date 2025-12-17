#Cacular e mostrar a hipotenusa tendo os catetos
from math import hypot, degrees, asin
cateto1 = float(input('Digite o valor do cateto adjacente: '))
cateto2 = float(input('Digite o valor do cateto oposto: '))
hip = hypot(cateto1,cateto2)
sen = degrees(asin(cateto2 / hip))
cossen = 90 - sen
print(f'Aqui estão os valores para os dados fornecidos:\n'
      f'hipotenusa = {hip:.2f};\n'
      f'seno = {sen:.2f}°;\n'
      f'cosseno = {cossen:.2f}°')
