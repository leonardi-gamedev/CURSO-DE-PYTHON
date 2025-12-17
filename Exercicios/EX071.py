# simular caixa eletronico, perguntar valor a ser sacado (inteiro)
# informar quantas cedulas de cada valor (50, 20, 10, 1)

while True:
    try:
        saque = int(input('Informe o valor do saque:'))
        if saque <= 0:
            print('O valor não pode ser zero ou negativo')
        else:
            break
    except ValueError:
        print('Valor inválido, digite novamente.')
notas_50 = saque // 50
resto_50 = saque % 50
notas_20 = resto_50 //20
resto_20 = resto_50 % 20
notas_10 = resto_20 // 10
resto_10 = resto_20 % 10
notas_01 = resto_10
s = 'SAQUE APROVADO'

print(f'\033[1;030;043m{s:=^45}\033[0;0;0m')
print(f'Valor solicitado R$ {saque}')
if notas_50 != 0:
    print(f'Quantidade de notas de 50: {notas_50}')
if notas_20 != 0:
    print(f'Quantidade de notas de 20: {notas_20}')
if notas_10 != 0:
    print(f'Quantidade de notas 10: {notas_10}')
if notas_01 != 0:
    print(f'Quantidade de notas 01: {notas_01}')
