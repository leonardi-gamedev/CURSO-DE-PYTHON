#ler um ano e falar se ele é bissexto
# Regras para Identificar um Ano Bissexto
# Divisível por 4:
#
# Um ano é bissexto se for divisível por 4.
# Exceto os anos múltiplos de 100:
#
# Anos divisíveis por 100 não são bissextos, a menos que...
# Sejam divisíveis por 400:
#
# Anos divisíveis por 400 são bissextos.

# Ler um ano e falar se ele é bissexto
ano = int(input('Digite o ano que quer verificar se é, foi ou será bissexto: '))

# Regras para identificar se é bissexto
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano} é bissexto.')
        else:
            print(f'O ano {ano} não é bissexto.')
    else:
        print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')