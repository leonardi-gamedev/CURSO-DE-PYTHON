# ler dados de varias pessoas (idade e genero)
# perguntar se o usuario quer continuar ou não
# mostrar: quantas pessoas tem mais que 18 anos. quantos homens e quantas mulheres com menos que 20.

from re import findall as achar

def ler_idade() -> int:
    while True:
        entrada = input('Informe a idade: ').strip()
        numerico = achar(r'-?\d+',entrada) #Retorna uma lista de números encontrados na string
        if numerico:    #Se a lista não esta vazia   
            idade = int(numerico[0]) # Pega o primeiro número encontrado
            if idade < 0:
                print('A idade não pode ser negativa')
                continue
            return idade #retorna como inteiro
        print('Idade inválida. Por favor digite um valor válido!')

def ler_genero() -> str:
    while True:
        entrada = input('Informe o gênero[M/F]:').strip().upper()
        if entrada and entrada[0] in 'MF':
            return entrada[0]
        else:
            print('Entrada inválida, Digite M ou F')

def parada() -> bool:
    while True:
        entrada = input('Deseja continuar [S/N?] ').strip().upper()
        if entrada and entrada[0] == 'N':
            return False
        elif entrada and entrada[0] == 'S':
            return True
        print('Resposta inválida!')

def main ():

    titulo = ' Entrada de Dados '
    print(f'{titulo:=^20}')

    pessoas_mais_18 = 0
    qtd_homens = 0
    mulher_menos_20 = 0

    while True:
        
        idade = ler_idade()
        genero = ler_genero()

        if idade > 18:
            pessoas_mais_18 += 1
        if genero == 'M':
            qtd_homens += 1
        if genero == "F" and idade<20:
            mulher_menos_20 +=1
        if not parada():
            break
    print(f'Existem {pessoas_mais_18} pessoas com mais que 18 anos.\n'
      f'Existem {qtd_homens} homens com menos que 20 anos.\n'
      f'Existem {mulher_menos_20} mulheres com menos que 20 anos')

main()





