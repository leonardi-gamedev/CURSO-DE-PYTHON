# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

#inicio = input('Digite qualquer coisa para iniciar a contagem   ')

for a in range (10,-1,-1):
    print(a)
    sleep(.7)

print(f'{"=~"*10}\n'
      f'FELIZ ANO NOVO!!!\n'
      f'{"=~"*10}')

