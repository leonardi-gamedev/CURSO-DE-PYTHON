print('Informe sua data de nascimento: ')
dia=int(input('Que dia você nasceu? '))
mes=int(input('Em qual mês? '))
ano=int(input('Em que ano? '))
#linha abaixo adicinada apos aula de listas
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

print('A data de nascimento informada é',dia,mes,ano)


print(f'Você nas em {dia} de {meses[mes - 1]} de {ano}')
