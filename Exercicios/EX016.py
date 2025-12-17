'''#Ler um número e mostrar a parte inteira ex 6.478 mostra 6
from math import trunc
num = float(input('Digite um número com 1 ou mais casas decimais: '))
resultado = trunc(num)
print(f'A parte inteira do número {num} é {resultado}')'''

num = float(input('Digite um número real: '))
print(f'A parte inteira do número {num} é {int(num)}')


