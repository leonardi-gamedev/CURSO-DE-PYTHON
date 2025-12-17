# Mostrar tabuada de vários números, um de cada vez conforme digitados
# interromper programa quando digitar um número negativo

titulo = ' TABUADA 3.0 '
print(f'{titulo:=^50}\n')
parar = ' \033[1;34mDigite qualquer valor negativo para parar \033[0m'
inicio = 1
erro = ' \033[1;31mValor inválido\033[0m '
tabuada = ' '
fim = ' \033[1;33mPROGRAMA FINALIZADO\033[0m '
print(f'{parar:=^61}\n')
print('=~'*25)
while True:
    if inicio == 1:
        num = input('Deseja ver a tabuada de qual número? ').strip()
        inicio = 0
    else:
        num = input('Deseja ver a tabuada de qual outro número? ').strip()
    if num.startswith('-') and num[1:].isnumeric():
        print(f'{fim:=^61}')
        break
    if num.isnumeric():
        num = int(num)
        for x in range(1,11):
            tabuada = f'{num:>6} x{x:3} = {num * x:<5}'
            print(f'{tabuada}')
    else:
        print(f'{erro:=^61}')
    print('=~'*25)