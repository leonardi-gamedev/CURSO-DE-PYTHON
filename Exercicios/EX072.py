# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
titulo = 'Números por Extenso'
c = 'S'
print(f'\033[1;30;43m{titulo:=^45}\033[0;0m')
cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while c == 'S':
    while True:
        try:
            num = int(input('Digite um número entre 0 e 20: '))
            if num < 0 or num > 20:
                print('\033[1;31;40mValor invalido, tente novamente.\033[0;0m')
                continue
            else:
                break
        except ValueError:
            print('\033[1;31;40mValor invalido, tente novamente.\033[0;0m')

    print(f'Você digitou o número \033[30;43m{cont[num]}\033[0;0m. ', end="")
    while True:
        try:
            c = input('Quer continuar? [S/N]').strip().upper()[0]
            if c in 'SN':
                break
        except ValueError:
            print('Digite apenas S ou N.', end='')
f = 'Programa encerrado'
print(f'\n\033[1;30;43m{f:=^45}\033[0:0m')