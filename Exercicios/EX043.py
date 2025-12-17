# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal // 25 até 30: Sobrepeso // 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida


print('\nOlá usuário, bem vindo ao programa de cálculo do IMC!\n')
peso = float(input('Informe o peso(Kg): '))
altura = float(input('Informe a altura(m): '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'O individuo possui IMC de {imc:.2f} e está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print(f'O individuo possui IMC de {imc:.2f} e está no PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'O individuo possui IMC de {imc:.2f} e está com SOBREPESO.')
elif 30 <= imc < 40:
    print(f'O individuo possui IMC de {imc:.2f} e está com OBESIDADE.')
else:
    print(f'O individuo possui IMC de {imc:.2f} e está com OBESIDADE MORBIDA.')