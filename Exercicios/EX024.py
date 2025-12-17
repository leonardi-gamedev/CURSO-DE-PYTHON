#Ler o nome da cidade e dizer se começa ou não com santo
cidade = input('Qual o nome da sua cidade? ').strip()
c2 = cidade.split()
range = ['santo','santa','são']
checar = c2[0].lower() in range
print(f'O nome da cidade digitada começa com Santo(a) ou São? {"Sim" if checar else "não"}')
