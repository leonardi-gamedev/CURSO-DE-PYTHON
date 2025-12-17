# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a nota da P1: '))
n2 = float(input('Digite a nota da P2: '))

media = (n1 + n2) / 2

if media >= 7.0:
    print(f'Você esta\033[32m APROVADO\033[0;0m,s ua média foi {media}.')
elif media < 5.0:
    print(f'Você está\033[31m REPROVADO\033[0;0m, sua média foi {media}.')
else:
    print(f'Você está de\033[33m RECUPERAÇÃO\033[0;0m, sua média foi {media}.')