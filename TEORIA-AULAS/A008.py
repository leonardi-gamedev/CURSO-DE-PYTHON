import math #Importe da biblioteca de formulas matemáticas
#Se for usar somente uma especifica 'from math import sqrt', assim não uso math.sqrt, só o sqrt
num = float(input('Digite um número qualquer: '))
raiz = math.sqrt(num) # se for importado sqrt apenas, não precisa do math.
print(f'A raiz quadrada de {num:.2f} é {raiz:.2f}')

