#Ler nome de 4 alunos e sortear uma ordem para apresentação
import random
n1 = str(input('Qual o nome do primero aluno? '))
n2 = str(input('Qual o nome do aluno seguinte? '))
n3 = str(input('Qual o nome do aluno seguinte: '))
n4 = str(input('Qual o nome do último aluno? '))
grupo = [n1, n2, n3, n4]
random.shuffle(grupo)
print(f'A ordem de apresentação será: {grupo}')
