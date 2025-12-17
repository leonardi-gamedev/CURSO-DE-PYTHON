#Perguntar salario e dar aumento de 10% para maior que 1250 (2024 atualizado) e 15% para menores


salario = float(input('Qual seu salário? '))
print(f'\nParabéns pelo aumento, seu salário será de R${1.1 * salario if salario >= 2024 else 1.15 * salario:.2f} a partir de 06/01/2025')
