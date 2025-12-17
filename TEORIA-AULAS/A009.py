#Manipulação de texto

frase= 'Curso em video Python'
print('\nAvaliando a frase "Curso em video Python"\n')
print(f'Resultado de frase[9] = {frase[9]};' #Retorna o caractere na posição 9, lembrando que inicia em 0
      f'\nfrase[9:13] = {frase[9:13]};' #Retorna o cadeia de caracteres 9 à 12
      f'\nfrase[9:21:2] = {frase[9:21:2]};' #retorna a cadeia mensionada pulando de 2 em 2
      f'\nfrase[::3] = {frase[::3]}'#quando o inicio/fim esta em branco ele busca desde o começo até o final da string
      f'\nfrase.find("deo") = {frase.find('deo')}' #Mostra onde se inicia o valor procurado
      f'\nfrase.find("Linha") = {frase.find('linha')}')

# len(), count(), find(), transformações com replace(), upper(),
# lower(), capitalize(), title(), strip(), junção com join().


