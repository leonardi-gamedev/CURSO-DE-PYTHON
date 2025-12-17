# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar
# a estrutura de repetição while no Python. Por exemplo:

from time import sleep

c = 1

while c!=10:
    print(c, end=' ► ')
    c += 1
    sleep(.5)
print('Acabou')