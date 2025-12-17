# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print(f"{' Jo Ken Po ':=^40}")

# Dicionário de jogadas
opcoes = {1:'Pedra',2:'Papel',3:'Tesoura'}

print('\nFaça sua escolha:\n'
      '[1] Pedra\n'
      '[2] Papel\n'
      '[3] Tesoura\n')

p = int(input('O que você escolhe: '))

# Escolha aleatória da CPU (chave do dicionário)
cpu = choice(list(opcoes.keys()))

print(f'\n{" HORA DO DUELO ":=^40}')
sleep(1)
print(f'Jogador -> {opcoes[p]}')
sleep(1)
print(f'CPU -> {opcoes[cpu]}')
sleep(1)
if p == cpu:
    print('O resultado é um \033[33mEMPATE\033[0;0m')
elif (p == 1 and cpu == 3) or (p == 2 and cpu == 1) or (p == 3 and cpu == 2):
    print('Você \033[32mVENCEU!\033[0;0m')
else:
    print('Você \033[31mPERDEU!\033[0;0m')



