# Exercício Python 080: Crie um programa onde o usuário possa
# digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numeros = []
print(f'lista = {numeros}')
for a in range(0,5):
    x = int(input('Digite um número inteiro: '))
    if a == 0 or x >= max(numeros):
        numeros.append(x)
        print(f'lista = {numeros}')
    elif x < min(numeros):
        numeros.insert(0,x)
        print(f'lista = {numeros}')
    else:
        for i, num in enumerate(numeros):
            if x < num:
                numeros.insert(i,x)
                print(f'lista = {numeros}')
                break
print('='*50)
print(f'Lista final: {numeros}')
