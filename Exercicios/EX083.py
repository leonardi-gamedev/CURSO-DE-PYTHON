# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses
# Seu aplicativo deverá analisar se a expressão passada esta com os parenteses abertos e fechados
# na ordem certa.

frase = str(input('Digite sua expressão: '))
p1 = []
for letra in frase:
    if letra == ')' and len(p1) == 0:
        p1.append('8')
        break
    elif letra=='(':
        p1.append(letra)
    elif letra==')':
        if len(p1)>0:
            p1.pop()
if len(p1) == 0:
    print(f'A expressão {frase} é válida!')
else:
    print(f'A expressão "{frase}" não é válida!')
