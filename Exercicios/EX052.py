# Exercício Python 52: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

titulo = ' Verificador de Núm. primo '

print(f'\n{titulo:=^55}')
num = int(input('Digite um número: '))

divisor = 1

if num <= 1:
    print(f'O número {num} não é primo.')
else:
    primo = True
    for x in range(2, num):
        resto = num % x
        #print(x) # usado apenas para testar x estava variando corretamente
        if resto == 0:
            primo = False
            divisor = x
            break

    if primo:
        print(f'O número {num} é somente divisível por 1 e por ele mesmo.\n'
              f'Portanto é um número primo.')
    else:
        print(f'O número {num} é divisível por {divisor}, portanto não é primo.')
