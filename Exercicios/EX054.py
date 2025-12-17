# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

c = 0

for x in range(0,7):
    ano_atual = int(datetime.date.today().year)
    nasc = int(input('Qual seu ano de nascimento? '))
    if ano_atual - nasc >= 21:
        c += 1

print(f'Dentre essas pessoas {c} são maiores de idade e {7 - c} são menores.')
