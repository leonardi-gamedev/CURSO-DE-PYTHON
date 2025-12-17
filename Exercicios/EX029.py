#recebe a velocidade de um carro, ate 80km/h de os parabens, acima disso informe que foi multado e o
#valor da multa R$7,00 para cada Km acima do limite


veloc = float(input('Informe a velocidade do veículo em Km/h: '))
print(f'A velocidade informada foi {veloc:.2f} Km/h, então: ')
if veloc < 81 :
    print(f'Veículo manteve a velocidade de {veloc:.2f} e não ultrapassou o limite da via.')
else:
    acima = veloc - 80
    multa = acima * 7
    print(f'Por estar {acima:.2f} km/h acima da velocidade permitida na via você foi multado\n'
          f'em R${multa:.2f}')

