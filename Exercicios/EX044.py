# Exercício Python 44: Elabore um programa que calcule
# o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('\nBem vindo ao gerenciador de pagamentos!\n')
valor = float(input('Informe o valor do produto: R$ '))
pag = int(input('Informe a condição de pagamento:\n'
                '[1] à vista no dinheiro / pix: 10% OFF.\n'
                '[2] à vista no cartão: 5% OFF.\n'
                '[3] em 2x no cartão: preço base\n'
                '[4] em 3x ou mais no cartão: 20% de juros.\n'))

if pag == 1:
    print(f'Pela condição de pagamento escolhida o produto ficará R${valor*0.9:.2f}')
elif pag == 2:
    print(f'Pela condição de pagamento escolhida o produto ficará R${valor*0.95:.2f}')
elif pag == 3:
    print(f'Pela condição de pagamento escolhida o produto ficará R${valor:.2f}\n'
          f'a ser pago em 2 x R${valor / 2:.2f}')
elif pag == 4:
    print(f'Pela condição de pagamento escolhida o produto ficará R${valor*1.2:.2f}\n')
    parc = int(input('Informe o número de parcelas (3 à 7): '))
    print(f'Será pago em {parc} x R${valor * 1.2 / parc:.2f}')
else:
    print(f'Opção inválida, favor escolher opção de pagamento.')
