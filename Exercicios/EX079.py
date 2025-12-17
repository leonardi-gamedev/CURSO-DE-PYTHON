#Exercício Python 079: Crie um programa onde o usuário possa digitar
# vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
loop = 1
while loop:
    #Validar entrada do número
    while True:
        try:
            x = int(input('Digite um número inteiro: '))
            if x in numeros:
                print(f'O número {x} existe na lista. Não adicionado.')
                break
            else:
                print(f'O número {x} foi adicionado.')
                numeros.append(x)
                break
        except ValueError:
            print('Valor invalido. Digite um número inteiro.')

    print(numeros)
    #Verificar se continua o loop
    while True:
        try:
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
        except ValueError:
            print('Digite um valor valido')

print(f'A lista tem {len(numeros)} elementos. ordenados a seguir:')
numeros.sort()
print(numeros)
