#Exercício Python 077: Crie um programa que tenha uma tupla
# com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

tupla =('sol','livro','montanha','coragem','vento',
        'esperanca','gato','musica','aurora','sussurro')
vogais = 'AEIOUaeiou'
titulo = 'SEPARADOR DE VOGAIS'
print(f'\033[1;30;43m{titulo:=^45}\033[0;0m')
for palavra in tupla:
    print(f'\nA palavra {palavra.upper()} contem as vogais: ',end='')
    achou = 0

    for letra in palavra:
        if letra in vogais:
            '''if achou == 1:  #Minha versão original
                print('-',end='')
                print(letra, end ='')
            elif achou == 0:
                print(letra,end='')
            achou = 1'''
            if achou:  #Versão simplificada, qualquer número diferente de zero é True
                print('-', end='')  # zero é false, então 'if achou' lê como falso
            print(letra, end='')
            achou = 1               # a partir daqui 'if achou' lê como verdadeiro e executa o hifen

