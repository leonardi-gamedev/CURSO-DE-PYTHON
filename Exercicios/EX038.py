# Comparar números A e B e dizer qual o maior ou se são iguais

primeiro = float(input("Digite o primeiro número: "))
segundo = float(input('Digite o segundo número: '))

if primeiro > segundo:
    print(f'O número {primeiro} é maior.')
elif primeiro < segundo:
    print(f'O número {segundo} é maior.')
else:
    print('Os números são iguais.')
