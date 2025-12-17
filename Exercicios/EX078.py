# Exercício Python 078: Faça um programa que leia 5 valores numéricos
# e guarde-os numa lista. No final, mostre qual foi o maior e
# o menor valor digitado e as suas respectivas posições na lista.

numeros = []

for a in range(0,5):
    numeros.append(int(input('Digite um número: ')))
maior = max(numeros)
menor = min(numeros)
pos_maior = numeros.index(maior)
pos_menor = numeros.index(menor)
print('=-'*25)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor foi {maior}', end = '')
for i, valores in enumerate(numeros): #nova solução
    if valores == maior:
        print(f' e na posição {i}', end = '')
'''if numeros.count(maior) > 1: # Solução inicial
    for b in range(0, numeros.count(maior)-1):
        print(f' e na posição {numeros.index(maior,pos_maior+1)}', end = '')
        pos_maior = numeros.index(maior,pos_maior+1)'''

print(f'\nO menor valor foi {menor}', end = '')
for j, valores in enumerate(numeros): #nova solução
    if valores == menor:
        print(f' e na posição {j}', end = '')
'''if numeros.count(menor) > 1: # Solução inicial
    for c in range(0, numeros.count(menor)-1):
        print(f' e na posição {numeros.index(menor, pos_menor+1)}', end = '')
        pos_menor = numeros.index(menor,pos_menor+1)'''
#print(numeros)