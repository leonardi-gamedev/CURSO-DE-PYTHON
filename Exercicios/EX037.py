# RECEBER UM NUMERO E CONVERTER PARA BINARIO, OCTAL OU EXADECIMAL

valor = int(input('Digite um número: '))
print('Escolha para qual base deseja fazer a conversão:\n'
      '[1] Binário\n'
      '[2] Octal\n'
      '[3] Hexadecimal')
x = int(input('Sua escolha: '))

if x == 1:
    print(f'Iniciando a conversão de {valor} para a base binária\n'
          f'O valor é {valor:b}') #bin(valor)[2:]
elif x == 2:
    print(f'Iniciando a conversão de {valor} para a base octal\n'
          f'O valor é {valor:o}') #oct(valor)[2:]
elif x == 3:
    print(f'Iniciando a conversão de {valor} para a base hexadecimal\n'
          f'O valor é {valor:X}') #hex(valor)[2:]
else:
    print('Escolha inválida.')