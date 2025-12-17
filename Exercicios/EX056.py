# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

media_idade = 0
h_velho = 0
q_m_nova = 0

for x in range (0,4):
    nome = input(f'\n{x+1}°Pessoa:\nInforme seu nome: ').strip().upper()
    idade = int(input('Informe sua idade: '))
    genero = input('Informe seu gênero (F ou M): ').strip().upper()
    media_idade = media_idade + idade / 4
    if genero == 'M':
        if idade > h_velho:
            h_velho = idade
            nome_h = nome
    elif genero == 'F':
        if idade < 20:
            q_m_nova += 1

print(f'\nA média de idade do grupo é {media_idade} anos')
if h_velho == 0:
    print('Não há homens no grupo.')
else:
    print(f'O homem mais velho é o Sr.{nome_h}')
if q_m_nova == 0:
    print('Não há mulheres no grupo.')
else:
    print(f'Tem {q_m_nova} mulheres com menos de 20 anos.')

