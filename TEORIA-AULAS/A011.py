#Adicionar cores
#ANSI - iniciar com \033[XX;X;XXm - XXXXX é a cor estilo / texto e fundo
#STYLE - 0 = nenhum, 1 = bold, 4 = underline, 7 = negative
#TEXT - Cor, vai de 30 à 37
#BACK - cor de fundo do 40 À 47

#\033[4;34;42m
print('\033[4;34;42mTeste\033[0m')
print('XXXX')
print('\033[4;34mTeste\033[0m')  # Sublinhado e azul
