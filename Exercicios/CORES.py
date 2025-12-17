''' vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'

branco = '\033[37m'

restaura cor original = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'

fundo preto = '\033[40m'
fundo vermelho = '\033[41m'
fundo verde = '\033[42m'
fundo amarelo = '\033[43m'
fundo azul = '\033[44m'
fundo magenta = '\033[45m'
fundo ciano = '\033[46m'
fundo branco = '\033[47m' '''

# Definição das cores (foreground)
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'

# Outros estilos
restaura = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'

# Definição das cores de fundo
fundo_preto = '\033[40m'
fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'
fundo_magenta = '\033[45m'
fundo_ciano = '\033[46m'
fundo_branco = '\033[47m'

# Dicionários para iteração
fg_colors = {
    'preto': preto,
    'vermelho': vermelho,
    'verde': verde,
    'amarelo': amarelo,
    'azul': azul,
    'magenta': magenta,
    'ciano': ciano,
    'branco': branco,
}

bg_colors = {
    'fundo_preto': fundo_preto,
    'fundo_vermelho': fundo_vermelho,
    'fundo_verde': fundo_verde,
    'fundo_amarelo': fundo_amarelo,
    'fundo_azul': fundo_azul,
    'fundo_magenta': fundo_magenta,
    'fundo_ciano': fundo_ciano,
    'fundo_branco': fundo_branco,
}

def mostra_fundos():
    print("=== Cores de fundo ===")
    for nome, code in bg_colors.items():
        # Texto em branco para visibilidade, se o fundo for claro talvez não contraste bem
        linha = f"{code}{branco} {nome} {restaura}"
        print(linha)
    print(restaura)

def mostra_textos():
    print("=== Cores de texto ===")
    for nome, code in fg_colors.items():
        linha = f"{code}{nome}{restaura}"
        print(linha)
    print(restaura)

def mostra_combinacoes():
    print("=== Combinações FG + BG ===")
    for bg_nome, bg_code in bg_colors.items():
        for fg_nome, fg_code in fg_colors.items():
            # Evita combinação igual FG=BG? Aqui mostramos mesmo assim.
            texto = f"FG:{fg_nome} BG:{bg_nome}"
            print(f"{fg_code}{bg_code}{texto}{restaura}", end='  ')
        print()  # nova linha por cada fundo
    print(restaura)

if __name__ == "__main__":
    mostra_fundos()
    mostra_textos()
    mostra_combinacoes()
