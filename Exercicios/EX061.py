# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''titulo = ' Progressão Aritmética(PA) '
print(f'\n{titulo:=^48}')
termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))

for x in range(1,11):
    pa = termo + (x - 1) * razao
    print(f'{pa}', end=' → ')

print('FIM')'''

titulo = ' Progressão Aritmética(PA) '
print(f'{titulo:=^48}')

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
pa = 0
x = 1

while x < 11:
    pa = t + (x - 1) * r
    print(f'{pa}', end = ' → ')
    x += 1

print('FIM')