#Ler um numero inteiro e mostrar se par ou impar

num = int(input('Digite um número inteiro: '))
resto = num % 2

if resto == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')

