def coletar_entradas():
    while True:
        escolha = input("Comprimento da barra (6 ou 12 metros)? ").strip()
        if escolha in ('6', '12'):
            comprimento_mm = int(escolha) * 1000  # em mm
            break
        else:
            print("Digite 6 ou 12.")
    cortes = []
    while True:
        entrada = input("Digite tamanho do corte em mm (ou Enter para finalizar): ").strip()
        if entrada == "":
            break
        try:
            tamanho = int(entrada)
            if tamanho <= 0:
                print("Tamanho deve ser positivo.")
                continue
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue

        qtd_str = input(f"Quantidade de peças de {tamanho} mm? ").strip()
        try:
            qtd = int(qtd_str)
            if qtd <= 0:
                print("Quantidade deve ser positiva.")
                continue
        except ValueError:
            print("Quantidade inválida.")
            continue

        cortes.append((tamanho, qtd))
    return comprimento_mm, cortes


def distribuir_pecas(bar_length, cortes):
    pecas = []
    for tamanho, qtd in cortes:
        if tamanho > bar_length:
            print(f"Atenção: peça {tamanho} mm maior que barra {bar_length} mm. Será ignorada.")
            continue
        pecas.extend([tamanho] * qtd)
    pecas.sort(reverse=True)
    barras = []
    for p in pecas:
        alocado = False
        for barra in barras:
            if p <= barra['restante']:
                barra['pecas'].append(p)
                barra['restante'] -= p
                alocado = True
                break
        if not alocado:
            barras.append({'pecas': [p], 'restante': bar_length - p})
    return barras


def main():
    bar_length, cortes = coletar_entradas()
    if not cortes:
        print("Nenhum corte informado. Saindo.")
        return
    barras = distribuir_pecas(bar_length, cortes)
    print("\nResultado do aproveitamento:")
    print(f"Total de barras necessárias: {len(barras)}")
    for idx, barra in enumerate(barras, start=1):
        print(f" Barra {idx}:")
        print(f"  Peças: {barra['pecas']}")
        print(f"  Sobra (mm): {barra['restante']}")
    total_sobra = sum(barra['restante'] for barra in barras)
    print(f"Sobra total acumulada (mm): {total_sobra}")
    input("\nPressione [Enter] para sair...")


if __name__ == "__main__":
    main()
