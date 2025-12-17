# Exercício Python 50: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
'''
lista = []

num = str(input('Digite seis números interos separados por vírgula: '))

lista.extend(int(valor.strip()) for valor in num.split(','))
s = 0
for a in range(0,6):
    if lista[a] % 2 == 0:
        s = s + lista[a]

print('\nA soma dos números pares da sequencia',lista,f'é {s}') '''

s = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n

print(f'A soma dos números pares é {s}')