#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

titulo = ' Progressão Aritmética(PA) '
print(f'{titulo:=^48}')

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
pa = 0
x = 1
b = 11
a = 0
while x != 0:
    pa = t + (x - 1) * r
    print(f'{pa}', end = ' → ')
    x += 1
    if x == b:
        print('...\n')
        a = int(input('Quer adicionar mais temos à PA?\n'
                  '[Informe a quantidade ou digite Zero para encerrar]: '))
        if a != 0:
            b = b + a
        else:
            x = 0
print('FIM!\n')
