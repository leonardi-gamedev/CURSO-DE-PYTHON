#Calcular preço da viagem, 0,5/km para ate 200 km e 0,45/km acima disso

dist = float(input('Quantos quilômetros foram percorridos? '))

if dist <= 200:
    print(f'O custo da viagem de {dist:.2f} km é de R${dist * 0.5:.2f}')
else:
    print(f'O custo para a viagem de {dist:.2f} km é de R${dist * 0.45:.2f}')
