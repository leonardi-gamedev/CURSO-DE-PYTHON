from unittest.mock import patch

def achar(padrao, texto):
    import re
    return re.findall(padrao, texto)

def ler_idade() -> int:
    while True:
        entrada = input('Informe a idade: ').strip()
        numerico = achar(r'-?\d+', entrada)
        if numerico:
            idade = int(numerico[0])
            if idade < 0:
                print('A idade não pode ser negativa')
                continue
            return idade
        print('Idade inválida. Por favor digite um valor válido!')

def testar_varias_entradas(entradas):
    try:
        with patch('builtins.input', side_effect=entradas):
            idade = ler_idade()
            print(f'Idade capturada: {idade}')
    except StopIteration:
        print('Faltaram entradas para completar o teste.')

# Teste com entradas
testar_varias_entradas([
    'abc', '-5', '', '  ', '12', '0', '100', '-100', 'idade: 30', '30 anos',
    'abc123xyz', 'a-15b', '9999999999', 'zero', '25.5', '1a2b3c', ' -7 ', '45', 'idade -1', 'idade 8'
])
