# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM // Até 14 anos: INFANTIL // Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR // Acima de 25 anos: MASTER

from datetime import date

ano_nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano_nasc

print(f'Você tem {idade} anos. \n')

if idade <= 9:
    print('Atleta irá competir na categoria \033[32mMIRIM\033[0;0m')
elif 9 < idade <= 14:
    print('Atleta irá competir na categoria \033[34mINFANTIL\033[0;0m')
elif 14 < idade <= 19:
    print('Atleta irá competir na categoria \033[35mJÚNIOR\033[0;0m')
elif 19 < idade <= 25:
    print('Atleta irá competir na categoria \033[36mSÊNIOR\033[0;0m')
elif 25 < idade:
    print('Atleta irá competir na categoria \033[33mMASTER\033[0;0m')
