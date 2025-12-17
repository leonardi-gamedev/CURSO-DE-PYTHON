#Ler 3 números e mostar qual é o maior e qual é o menor

print(' Digite três números e irei responder qual o maior e qual o menor!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o próximo número: '))
n3 = int(input('Digite o último número: '))
ordem = sorted ([n1, n2, n3])

print(f'Os seguintes números foram digitados {n1, n2, n3}\n'
      f'dentre estes {ordem[2]} é o maior \n'
      f'e o número {ordem[0]} é o menor.')