#Ex que detalha as propriedades do meu input
x = input('Digite algo: ')
print(f'O tipo desse valor é {type(x)}')
print(f'Só tem espaços? {x.isspace()}')
print(f'Só tem letras? {x.isalpha()}')
print(f'Só tem números? {x.isnumeric()}')
print(f'É inteiro? {x.isdecimal()}')
print(f'Só tem minúsculas? {x.islower()}')
print(f'Só tem maiúsculas? {x.isupper()}')
