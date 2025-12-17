#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

tupla = ()
b = 0
t = -1
'''tupla = (int(input(f'Digite o 1° número entre 1 e 10:')),
int(input(f'Digite o 2° número entre 1 e 10:')),
int(input(f'Digite o 3° número entre 1 e 10:')),
int(input(f'Digite o 4° número entre 1 e 10:')))'''

for i in range(0,4):
    while True:
        try:
            a = int(input(f'Digite o {i+1}° número entre 1 e 10:'))
            if a < 1 or a > 10:
                print('Valor fora do intervalo permitido.',end=' ')
            else:
                if a == 3 and t == -1:
                    t = i
                tupla += (a,)
                break
        except ValueError:
            print('Valor inválido.',end=' ')

print('=~' * 18)
print(f'Lista armazenada: {tupla}')
print('=~' * 18)
print(f'O número 9 foi digitado {tupla.count(9)} vezes.')
print('=~' * 18)
if t != -1:
    print(f'O número três foi digitado na primeira vez na posição {t+1}')
else:
    print('O número três não foi digitado')
print('=~' * 18)
for j in tupla:
    if j % 2 == 0:
        print(f'O número {j} é par.')
        b = 1
if b == 0:
    print('Não há números pares')

