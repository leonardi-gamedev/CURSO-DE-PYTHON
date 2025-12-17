# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nasc = int(input('Em que ano você nasceu? '))
ano_atual = int(date.today().year)
# print(date.today())
# print(f'{ano_atual}')

alist = ano_atual - ano_nasc

if alist > 18:
    print(f'Você está em situação irregular com o alistamento obrigatório,\n'
          f'neste ano você completa {alist} anos, está {alist - 18} anos atrasado.')
elif alist < 18:
    print(f'Ainda não é o momento de você se alistar,\n'
          f'faltam {18 - alist} anos.')
else:
    print('Este ano você completa 18 anos de idade, portanto deve se alistar\n'
          'para o serviço militar até junho!')
