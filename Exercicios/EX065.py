#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se
# ele quer ou não continuar a digitar valores.

titulo = ' Avaliador de Números Inteiros '
print(f'{titulo:=^45}')

num = int(input('Digite um número inteiro: '))
maior = menor = soma = num
termos = 1
c = True
opcao = ' '

while c:
    num_2 = int(input('Digite outro número: '))
    opcao = ' '
    soma += num_2
    termos += 1
    if maior < num_2:
        maior = num_2
    if menor > num_2:
        menor = num_2
    while opcao not in 'NnSs':
        opcao = str(input('Quer continuar? [S/N] ')).strip()
        if opcao not in 'SsNn':
            print('Valor inválido! responda com S ou N.')
    if opcao in 'Ss':
        c = True
    else:
        c = False
print(f'A média dos números é {soma / termos}')
print(f'o maior número é {maior} e o menor é {menor}')