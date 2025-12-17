# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = int(input('Digite o comprimento do segmento AB: '))
b = int(input('Digite o comprimento do segmento BC: '))
c = int(input('Digite o comprimento do segmento AC: '))

if a < b + c and b < a + c and c < b + a:
    if a == b == c:
        print('Os segmentos indicados formam um triângulo equilátero.')
    elif a == b or a == c:
        print('Os segmentos indicados formam um triângulo isósceles.')
    else:
        print('Os segmentos indicados formam um triângulo escaleno.')

else:
    print('Os segmentos indicados não formam um triângulo.')