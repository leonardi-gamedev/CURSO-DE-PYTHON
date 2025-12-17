# Ler varios números inteiros
# Parar quando digitar 999
# Mostrar quantidade de números digitados e soma, desconsiderando o 999

titulo = ' Leitor de Remessa '
print(f'{titulo:-^50}')
print('*****[Digite \033[7m999\033[0m para encerrar o programa]*****')
print('-' * 50)
qtd = 0
soma = 0
erro = ' \033[1;31;47mEntrada inválida\033[0m '
fim = ' \033[33mPROGRAMA FINALIZADO\033[0m '
while True:
    num = input(f'Digite a quantidade de itens na {qtd + 1}°NF: ')
    if num.isnumeric():
        num = int(num)
        if num == 999:
            print(f'{fim:=^50}')
            break
        soma += num
        qtd += 1
        print('-'*50)
    else:
        print(f'{erro:=^65}')
print(f'\nForam inseridos dados de \033[1;32m{qtd}\033[0m NFs no sistema.')
if soma != 0:
    print(f'\nO total de itens recebidos foi \033[1;32m{soma}\033[0m.')



