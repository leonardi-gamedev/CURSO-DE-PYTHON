#Definir tamanho de Barra 6/12m
#Ler o tamanho de corte e quantidade
#Fazer a distribuição na barra


def entradas():
    while True:
        try:
            tam_barra = int(input('Selecione o tamanho da barra[6/12]: '))
            tam = (6,12)
            if tam_barra not in tam:
                print('Tamanho inválido! Escolha 6 ou 12 metros.')
            else:
                tam_barra = tam_barra * 1000 #converter m para mm
                break
        except ValueError:
            print('Digite apenas 6 ou 12!')
    print(f'Tamanho da barra selecionado: {tam_barra} mm')
    cortes = []
    while True:
        corte = input('Digite o tamanho do corte[mm] ou tecle [Enter] para encerrar: ')
        if corte == '':
            break
        try:
            corte = int(corte)
            if corte < 1:
                print('O tamanho de corte não pode ser negativo ou nulo.')
                continue
            if corte > tam_barra:
                print(f'O tamanho do corte {corte} mm é maior do que a barra selecionada.\n'
                      f'Entrada ignorada.')
                continue
        except ValueError:
            print('Digite um valor inteiro!')
            continue
        try:
            qtd = int(input(f'Digite a quantidade de peças de {corte} mm: '))
            if qtd < 1:
                print('Quantidade não pode ser nula ou negativa!')
                continue
            else:
                cortes.append((corte, qtd))
        except ValueError:
            print('Digite um valor inteiro.')
    return (cortes, tam_barra)

cortes, tam_barra = entradas()

def executar(cortes, tam_barra):
    cortes_decr = sorted(cortes, key = lambda c: c[0], reverse=True)
    barras = []
    pecas = []
    for item in cortes_decr:
        print(item[0])
        pecas.extend([item[0]] * item[1])
        print(pecas)
        for b in range(0,item[1]):
            sobra = tam_barra - item[0]
            barras.append
    #for id in cortes_decr:




    return cortes_decr, barras
cortes_decr, barras = executar(cortes, tam_barra)
print('='*30)
print(cortes)
print(tam_barra)
print(cortes_decr)
print('='*30)

