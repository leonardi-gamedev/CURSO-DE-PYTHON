#Ler 4 nomes, sortear e mostrar um deles
from random import choice
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno seguinte: '))
aluno3 = str(input('Digite o nome do aluno seguinte: '))
aluno4 = str(input('Digite o nome do aluno seguinte: '))
grupo = [aluno1, aluno2, aluno3, aluno4]
sort = choice(grupo)
print(f'O aluno soteado para tarefa é: {sort}')

