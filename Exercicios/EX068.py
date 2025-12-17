# fazer programa que jogue par ou impar
# Interromper quando perder
# mostrar numero de vitórias consecutivas
from random import randint
from time import sleep

print('\33[1;32m=~'*21)
titulo = ' GAME: KENSU(拳数) '
print(f'{titulo:-^41}')
print('=~'*21)
print('\033[0m')
cpu = 0
resultado = 0
vitorias = 0
while True:
    mao = str(input('Escolha um número entre 0 e 10: ')).strip()
    if mao.isnumeric() and (0 <= int(mao) <= 10):
        mao = int(mao)
        kensu = str(input('Escolhe par ou ímpar [P/I]: ')).strip()
        if kensu == "":
            kensu = 'e'
        kensu = kensu[0]
        while kensu not in 'PpIiÍí':
            print('Entrada inválida, escolha PAR ou IMPAR. ')
            print('-' * 50)
            kensu = str(input('Escolhe par ou ímpar [P/I]: ')).strip()
            if kensu == "":
                kensu = 'e'
            kensu = kensu[0]
        if kensu in 'Pp':
            print('Escolha confirmada. Você selecionou PAR.')
        elif kensu in 'IiÍí':
            print('Escolha confirmada. Você escolheu IMPAR.')
        print('-'*50)
        cpu = randint(0, 10)
        resultado = (mao + cpu) % 2
        if resultado == 0 and kensu.lower() == 'p':
            print(f'Você jogou {mao} e o Computador jogou {cpu}.\n'
                  f'{mao} + {cpu} = {mao + cpu} (PAR).\n'
                  f'Então você GANHOU!!!!')
            print('-' * 50)
            vitorias += 1
        elif resultado == 1 and (kensu in 'IiÍí'):
            print(f'Você jogou {mao} e o Computador jogou {cpu}.\n'
                  f'{mao} + {cpu} = {mao + cpu} (IMPAR).\n'
                  f'Então você GANHOU!!!!')
            print('-' * 50)
            vitorias += 1
        elif resultado == 0 and (kensu in 'IiÍí'):
            print(f'Você jogou {mao} e o Computador jogou {cpu}.\n'
            f'{mao} + {cpu} = {mao + cpu} (PAR).\n'
            f'Então você PERDEU!.\n'
            f'Número de vitórias consecutivas = {vitorias}.')
            break
        else:
            print(f'Você jogou {mao} e o Computador jogou {cpu}.\n'
                  f'{mao} + {cpu} = {mao + cpu} (IMPAR).\n'
                  f'Então você PERDEU!.\n'
            f'Número de vitórias consecutivas = {vitorias}.')
            break
    else:
        print('Entrada inválida, escolha um número válido. ')
        print('-' * 50)
