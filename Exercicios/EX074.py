#Exercício Python 074: Crie um programa que vai gerar
# cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

import random
titulo = 'Gerador de números aleatórios'
print(f'\033[1;30;43m{titulo:=^45}\033[0;0m')
num = tuple(random.randint(1,1500) for a in range(0,5))
print('Segue a lista de números aleatórios gerados:')
print(num)
print('=~=~'*12)
print(f'O menor número da lista é {sorted(num)[0]}.')
print(f'O maior número da lista é {sorted(num)[-1]}')

f = 'Programa Finalizado'
print(f'\033[1;30;43m{f:=^45}\033[0;0m')