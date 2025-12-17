# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for x in range(0,5):
    peso = float(input(f'Qual o peso da {x+1}° pessoa?'))
    if x == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'Dentre essas pessoas o maior peso é {maior:.2f} Kg e o menor peso é {menor:.2f} Kg')