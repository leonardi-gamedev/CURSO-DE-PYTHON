#Ler uma frase e avaliar quantas vezes aparece a letra A, posição que aparece primeiro
# e a ultima posição que aparece
frase = input('Digite uma frase qualquer: ').strip()
#nc = len("".join(frase.split()))
#print(frase)
#print(nc)
#grupo = ['a','ã','â','á','à','ä']
contar = (frase.lower()).count('a')
print(f'Na frase "{frase}":')
print(f'A letra "a" aparece {contar} vezes.')
pvez = (frase.lower()).find('a') + 1
print(f'A primeira vez que ela parece é na posição {pvez}')
uvez = (frase.lower()).rfind('a') + 1
print(f'A útima vez que aparece é na posição {uvez}')