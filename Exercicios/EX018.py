#Dado um ângulo, mostrar seno, cosseno e tangente
from math import radians, sin, cos, tan
ang = float(input('Informe o valor do ângulo em graus(°): '))
rad = radians(ang)
seno = sin(rad)
coss = cos(rad)
tang = tan(rad)
print(f'Para o ângulo de {ang:.2f}° temos:\n'
      f'seno = {seno:.2f};\n'
      f'cosseno = {coss:.2f};\n'
      f'tengente = {tang:.2f};')