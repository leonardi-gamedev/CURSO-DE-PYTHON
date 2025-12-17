#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

from time import sleep

titulo = ' FATORIAL '
print(f'\033[34m{titulo:=^50}\033[0;0m')

t = int(input('Digite um número para calcular seu fatorial: '))
f = t
print(f'\n{f}! = {f} ',end="")
while t > 1:
    #print(f'{f}! = ')
    f = f * (t - 1)
    print(f'x {t - 1} ',end="")
    t -= 1
    #sleep(1)
print(f'= {f}')
print('\033[34m='*50)