#ler o nome completo e depois mostrar o 1° e o ultimo nome
nome = input('Digite seu nome completo: ').strip()
pesp = nome.find(' ')
primeiro_nome= nome[:pesp]
uesp = nome.rfind(' ')
ultimo_nome= nome[uesp + 1:]
print('Olá usuário!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')