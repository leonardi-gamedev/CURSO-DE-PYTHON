#Ler um número inteiro e fazer a tabuada
n= int(input('Digite um número inteiro: '))
print('~'* 40)
print(f'{n} x {1:2} = {n:<6}  {n} x {2:2} = {n*2:<6}\n{n} x {3:2} = {n*3:<6}  {n} x {4:2} = {n*6:<6}'
      f'\n{n} x {5:2} = {n*5:<6}  {n} x {6:2} = {n*6:<6}\n{n} x {7:2} = '
      f'{n*7:<6}  {n} x {8:2} = {n*8:<6} \n{n} x {9:2} = {n*9:<6}  {n} x {10:2} = {n*10:<6}')
print('~'* 40)
