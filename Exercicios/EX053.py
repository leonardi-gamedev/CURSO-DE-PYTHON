# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite sua frase: ').strip().lower()
#print(frase)
texto = ''.join(frase.split())
#print(texto)
#print(texto[::-1])
if texto == texto[::-1]:
    print(f'A frase "{frase}" é um palíndromo.')
else:
    print(f'A frase "{frase}" não é um palíndromo')