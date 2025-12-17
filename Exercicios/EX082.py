# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
impar = []
par = []
loop = 1
while loop:
    while True: # Validação da entrada e separação
        try:
            x = int(input('Digite um número inteiro: '))
            numeros.append(x)
            if x % 2 == 0:
                par.append(x)
            else:
                impar.append(x)
            print(f'O número {x} foi adicionado!')
            print('='*50)
            break
        except ValueError:
            print('Digite um valor válido.')
            print('=' * 50)

    while True: #Validação para continuar
        try:
            continuar = input('Deseja continuar? [S/N] ').strip().upper()
            if continuar in 'SN':
                if continuar == 'N':
                    loop = 0
                break
            else:
                print('Digite apenas S ou N.')
                print('=' * 50)
        except ValueError:
            print('Digite apenas S ou N')
            print('='*50)

print('~='*25)
print(f'A lista de números digitada foi {numeros}')
print(f'Destes, os seguintes são ímpares: {impar}')
print(f'E os seguintes são pares: {par}')
