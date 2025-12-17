#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random
import time

escolha = random.randint(0,10)
f = ' FIM '
m = ' PENSANDO '
tit = ' JOGO DA ADIVINHAÇÃO '
print(f'{tit:=^40}'.replace('=','=~'))
print('Irei escolher um número entre 0 e 10, tente adivinhar qual é.')
print(f'\033[33m{m:=^15}\033[0;0m'.replace('=','=~'))
time.sleep(1)
print('ESCOLHIDO!!!')
time.sleep(1)
palpite = int(input('Sua vez, em qual número eu pensei? '))
tentativas = 1

while palpite != escolha:
    palpite = int(input(f'Parece que você \033[31mERROU\033[0;0m, eu não pensei no número {palpite}'
                        f'\nTente de novo: '))
    tentativas += 1

print(f'Você \033[32mACERTOU!!!\033[0;0m Eu pensei no número {escolha}.'
      f'\n Foram necessárias {tentativas} tentativas.')
print(f'{f:=^60}')


