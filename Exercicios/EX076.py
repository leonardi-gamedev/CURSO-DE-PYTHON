#Crie um programa que tenha uma tupla única com nomes de
# produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Maçã (Un.)',4.50,'Leite (1L)',6.90,'Arroz (5 Kg)',22.00,
            'Feijão (1Kg)',8.75,'Pão (1Kg)',17.70,'Café(300g)',18.50,
            'Açúcar(1Kg)',5.60,'Ovo (15 Un.)',16.00,'Manteiga (250g)',12.30,
            'Queijo Prato (1Kg)',45.90)

titulo = 'Supermercado Ultra'
print(f'\033[1;30;43m{titulo:=^45}\033[0;0m')
for a in range(0, len(produtos), 2):
    print(f'{produtos[a]:.<36}R${produtos[a+1]:>7.2f}')