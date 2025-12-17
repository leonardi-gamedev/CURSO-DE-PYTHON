titulo = ' Avaliador de Números Inteiros '
print(f'{titulo:=^45}')

num = int(input('Digite um número inteiro: '))
maior = menor = soma = num
termos = 1
opcao = ' '
while opcao not in 'NnSs':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao not in 'SsNn':
            print('Valor inválido! responda com S ou N.')

while opcao in 'S':
    num_2 = int(input('Digite outro número: '))
    soma += num_2
    termos += 1
    if maior < num_2:
        maior = num_2
    if menor > num_2:
        menor = num_2
    opcao = ' '
    while opcao not in 'NnSs':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao not in 'SsNn':
            print('Valor inválido! responda com S ou N.')
    if opcao in 'Ss':
        c = True
    else:
        c = False
print(f'A média dos números é {soma / termos}')
print(f'o maior número é {maior} e o menor é {menor}')