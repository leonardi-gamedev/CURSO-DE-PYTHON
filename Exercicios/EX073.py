# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Mirassol.

times = ('Flamengo', 'Cruzeiro', 'RB Bragantino',
         'Palmeiras', 'Fluminense', 'Botafogo', 'Bahia',
         'Mirassol', 'Atlético-MG', 'Ceará', 'Corinthians',
         'Grêmio', 'São Paulo', 'Internacional', 'Vasco', 'Vitória',
         'Fortaleza', 'Santos', 'Juventude', 'Sport')
times_alf = sorted(times)
pos = times.index('Mirassol')
titulo = 'Campeonato Brasileiro'
print(f'\033[1;30;43m{titulo:=^45}\033[0;0m')
print('Os primeiros Colocados são:\n')
#print(f'Os 5 primeiros são: {times[0:5]}')
for a in range(0,5):
    print(f'{a+1}° colocado {times[a]}')
print('=' * 45)
print('Os ultimos colocados são:\n')
for b in range(16,20):
    print(f'{b+1}°Colocado: {times[b]}')
print('=' * 45)
print('Segue lista em ordem alfabética:\n')
print(times_alf)
print('=' * 45)
print(f'\n O Time do Mirassol esta na {pos+1}° Posição.')