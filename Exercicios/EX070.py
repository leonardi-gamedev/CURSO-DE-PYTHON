# Ler nome e preço de produtos
# perguntar se utilizador quer continuar
# mostrar total da compra, quantos produtos custam mais que mil, nome do produto mais barato

total_compra = mais_mil
mais_barato = float('inf')
nome_barato = ''
titulo = 'Resumo de Compras'
fim = 'Programa Encerrado'
print(f'\033[1;30;43m{titulo:=^40}\033[0;0m')

while True:
    while True: #Validação do nome do produto
        nome_produto = input('Digite o nome do produto: ')
        if nome_produto == "":
            print('O nome não pode estar vazio!')
        elif nome_produto.isdigit():
            print('O nome não pode conter apenas números!')
        else:
            break
    while True: #Validação do preço
        preco_str = input('Digite o preço do produto: R$')
        if preco_str == "":
            print('O preço não pode ser vazio! Digite novamente.')
            continue
        try:
            preco_produto = float(preco_str.replace(',', '.'))
            if preco_produto < 0:
                print(f'O preço não pode ser um valor negativo! Digite novamente.')
            else:
                break
        except ValueError:
            print('Valor inválido, digite novamnete')

    total_compra = preco_produto + total_compra
    if preco_produto > 1000:
        mais_mil += 1
    if preco_produto < mais_barato:
        nome_barato = nome_produto
        mais_barato = preco_produto
    while True:
        continuar = input('Deseja continuar? [S/N]').strip()
        if continuar == '' or continuar[0] not in 'SsNn':
            print('Por favor, digite S para continuar ou N para encerrar o programa.')
            continue
        if continuar[0] in 'SsNn':
            break
    if continuar[0] in 'Nn':
        break

print(f'{mais_mil} produtos custam mais que R$ 1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R$ {mais_barato:.2f}')
print(f'Total da compra R$ {total_compra:.2f}')
print(f'\033[1;30;43m{fim:=^40}\033[0;0;m')