#Ler um número entre 0 e 9999 e mostrar cada digito separado
# unidade/dezena/centena/milhar
#Fazer por string e por calculo
n = input('Digite qualquer número entre 0 e 9999: ')
completar = n.zfill(4)
print(f'O número fornecido foi : {n}, assim temos que: '
      f'\n unidade: {completar[3]};'
      f'\n dezena : {completar[2]};'
      f'\n centena: {completar[1]};'
      f'\n milhar : {completar[0]}.')


#Metodo matematico
'''n = int(input('Digite qualquer número entre 0 e 9999: '))

# Extraindo os dígitos com divisão e módulo
unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print(f'O número fornecido foi : {n}, assim temos que: '
      f'\n unidade: {unidade};'
      f'\n dezena : {dezena};'
      f'\n centena: {centena};'
      f'\n milhar : {milhar}.')
'''