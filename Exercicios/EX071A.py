# simular caixa eletronico, perguntar valor a ser sacado (inteiro)
# informar quantas cedulas de cada valor (50, 20, 10, 1)

c = (200,100,50,20,10,5,2,1)
i = 0
notas = []
titulo = 'Olá Querido Cliente'
print(f'\033[1;30;44m{titulo:=^45}\033[0;0m')
while True:
    try:
        saque = int(input('Informe o valor do saque:'))
        if saque <= 0:
            print('O valor não pode ser zero ou negativo')
        else:
            break
    except ValueError:
        print('Valor inválido, digite novamente.')
total = saque
while i < len(c):
   qtd = saque // c[i]
   notas.append(qtd)
   saque = saque % c[i]
   i += 1

s = 'SAQUE APROVADO'
print(f'\033[1;030;043m{s:=^45}\033[0;0;0m')
print(f'Valor solicitado R$ {total}')
print('Sairão as notas:')
for b in range(0, len(c)):
    if notas[b] != 0:
        print(f'{notas[b]:3} cédulas de R$ {c[b]:4},00')
f = 'OBRIGADO PELA PREFERÊNCIA'
print(f'\033[1;030;043m{f:=^45}\033[0;0;0m')

