#Receber nome completo e mostrar maiusculo, minusculo
# e qtd de letras sem espaços, qtd letras 1 nome
nome=input('Qual o seu nome completo? ').strip()
print(f'Nome do usuário: {nome}')
print(f'Nome em maiúscula: {nome.upper()}')
print(f'Nome em minúscula: {nome.lower()}')
texto = ''.join(nome.split())
qte = len(texto)
print(f'O Nome possui {qte} letras')
t2 = nome.split()
qtd = len(t2[0])
print(f'O primeiro nome possui {qtd} letras')