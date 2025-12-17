#Calcular o preço do aluguel de um carro R$60/dia R$0.15/Km

a=int(input('Por quantos dias o carro foi alugado? '))
b=float(input('Quantos quilomêtros foram rodados? '))
t = 60 * a + 0.15 * b
print(f'Pela utilização de {a} dias e {b} Km do veículo,\no total a pagar '
      f'será R${t:.2f} ')