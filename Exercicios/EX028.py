#Escreva um program que faça o computador escolher um número (0 a 5) para o usuário tentar acertar
#resultado informa se acertou o numero

import random

num = random.randint(0,5)
print('~-~-~-' * 15)
escolha = int(input('Descubra em qual número entre 0 e 5 estou pensando, qual seu palpite? '))
print('~-~-~-' * 15)
if num == escolha:
    print(f'Parabéns, você acertou! Eu pensei no número {num}')
else:
    print(f'Infelizmente você não acertou, eu pensei no número {num}')

#print(num)
