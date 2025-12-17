# Dado 3 segmentos de reta, informar se é possivel fazer um triangulo
# dado lados a, b e c a soma de quaisquer dois deles deve ser maior que o terceiro
import time

print('-=-' * 25)
print('\nOlá usuário, vamos verificar se 3 segmentos de reta formam um triângulo,\n'
      'para isso, digite três valores: \n')
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite o último número: '))
#print('\n')
print('-=-' * 25)
print('\n AVALIANDO VARIÁVEIS INSERIDAS...\n')
time.sleep(2)
if a + b > c and a + c > b and b + c > a:
    print(f'Sim, é possível formar um triangulo a partir de lados {a:.1f}, {b:.1f} e {c:.1f}')
else:
    print(f'Não é possivel construir um triângulo com {a:.1f}, {b:.1f} e {c:.1f}')