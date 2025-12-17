# 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

t = int(input('Mostrar a tabuada de qual número? '))
titulo = f' TABUADA DO {t} '

print(f'{titulo:=^25}')
for a in range(1,11):
    b = a * t
    linha = f'|{a:2} x {t:2} = {b:3} |'
    print(f'{linha:^25}')

print('='*25)