#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = 0

while c != 5:
    print('='*25)
    print('Qual operação deseja fazer:\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair')
    print('=' * 25)
    e = int(input('Sua escolha:  '))
    print('='*25)
    if e == 1:
        print(f'A soma dos valores: {a} + {b} = {a + b}')
    elif e == 2:
        print(f'A multiplicação dos valores: {a} x {b} = {a * b}')
    elif e == 3:
        if a > b:
            print(f'Dentre os dois números {a} é maior')
        elif a == b:
            print('Os números são iguais.')
        else:
            print(f'Dentre os dois números {b} é maior')
    elif e == 4:
        a = float(input('Digite novamente o 1° valor: '))
        b = float(input('Digite agora o 2° valor: '))
    elif e == 5:
        print('Finalizando o programa...')
        sleep(1)
        print('........')
        sleep(1)
        print('.....')
        sleep(1)
        print('Programa encerrado!')
        c = 5
    else:
        print('Valor inválido, digite outro!')
        # a = float(input('Digite novamente o 1° valor: '))
        # b = float(input('Digite agora o 2° valor: '))
