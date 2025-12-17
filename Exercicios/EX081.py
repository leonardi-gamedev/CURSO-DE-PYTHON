#Exercício Python 081: Crie um programa que vai ler vários
# números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []
loop = 1
while loop:
    #Validar entrada do número
    while True:
        try:
            x = int(input('Digite um número inteiro: '))
            print(f'O número {x} foi adicionado a lista.')
            print('='*50)
            numeros.append(x)
            break
        except ValueError:
            print('Valor invalido. Digite um número inteiro.')
    #Validar se interrompe o laço
    while True:
        c = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if c == '':
            print('Este campo não pode ser vazio. Digite novamente.')
            print('=' * 50)
        elif c[0] not in 'SN':
            print('Digite apenas S ou N')
            print('='*30)
        elif c[0] == 'N':
            loop = 0
            break
        else:
            break
print('~='*25)
print(f'\nA lista tem {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Lista em ordem decrescente= {numeros}')
if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')