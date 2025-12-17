#Aprovar um emprestimo, perguntar o valor da casa, salario e em quantos anos pagar
#calcular a prestação mensal e se exceder 30% negar emprestimo

p = float(input("Informe o valor da casa (R$): "))
salario = float(input('Informe seu salário (R$): '))
anos = float(input("Em quantos anos pretende pagar (máximo 35 anos)? "))
n = anos * 12
#prestacao = casa / (tempo * 12)
psal = 0.3 * salario
i = float(input('Informe a taxa de juros anual(%): '))
j = i / 12 / 100
a = p * (j * ( 1 + j ) ** n) / (( 1 + j ) ** n - 1)
print(f'A taxa de juros atual é de {j * 100:.2f}% ao mês. Você pagará R$ {a * n:.2f} ao final do prazo.')
print(f'Dado seu salário, o valor máximo da prestação poderá ser de R$ {psal:.2f}, logo:')
if a > psal:
    print(f'Empréstimo negado, a parcela seria de R$ {a:.2f}, tente dar uma entrada maior.')
else:
    print(f'Valor autorizado, você pagará R$ {a:.2f} por {anos:.2f} anos. Tenha um ótimo dia')
