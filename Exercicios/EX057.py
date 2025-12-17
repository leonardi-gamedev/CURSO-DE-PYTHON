#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

g = 0

while g != 'M' and g != 'F':
    g = input('Informe seu gênero [M/F]: ').strip().upper()
    if g != 'M' and g != 'F':
        print('Insira um valor válido, "M" para masculino e "F" para feminino.\n')

