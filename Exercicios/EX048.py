# Exercício Python 48: Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
c = 0
for a in range(0,501,3):
    if (a % 2) != 0:
        s += a
        c += 1
print(s)
print(c)