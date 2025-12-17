#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

titulo = ' Progressão Aritmética(PA) '
print(f'\n{titulo:=^48}')
termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))

for x in range(1,11):
    pa = termo + (x - 1) * razao
    print(f'{pa}', end=' → ')

print('FIM')