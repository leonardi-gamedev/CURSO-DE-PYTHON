#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados
#e qual foi a soma entre eles (desconsiderando o flag).

n = cont = soma = 0

print('\n')
print("=~"*10,end='')
print(' Contador e Soma ',end='')
print('=~'*10)
print('\n Digite 999 para encerrar o programa.\n')

while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n

print(f'\n Foram digitados {cont - 1} números, e a '
      f'\nsua soma é {soma - 999}')
