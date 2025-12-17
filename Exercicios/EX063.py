# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

titulo = ' Sequência de Fibonacci '

print(f'\n{titulo:=^50}')
a0 = 0
a1 = 1
n = int(input('Informe a quantidade de números\na '
              'serem mostrados: '))
cont = 2
print('0 → 1',end='')
while n != cont:
    print(f' → {a0 + a1}',end='')
    a1 = a0 + a1
    a0 = a1 - a0
    cont +=1
print('\n\nFIM!')

