#ler o nome e dizer se tem Silva
nome = input('Digite seu nome: ')
check = 'silva' in nome.lower()
print(f'\nO nome digitado {'' if check else 'não '}possui Silva.')