def acidentes_f():
    veiculos, acidentes, acidentes_2000 = [], [], []
    for cidade in range(1, 6):
        print(f'\nCidade: {cidade}:')
        num_veic_p = int(input('\ninforme o numero de veiculos de passeio (em 1999): '))
        veiculos.append(num_veic_p)
        num_acid_v = int(input('informe o numero de acidentes com vitimas (em 1999): '))
        if num_acid_v < 2000:
            acidentes_2000.append(num_acid_v)
        else:
            acidentes.append(num_acid_v)
    i_cid_maior_acid = acidentes.index(max(acidentes))
    i_cid_menor_acid = acidentes.index(min(acidentes))
    print(f'\nCidade com menor numero de acidentes: {i_cid_menor_acid + 1}, com {min(acidentes)}.')
    print(f'Cidade com maior numero de acidentes: {i_cid_maior_acid + 1}, com {max(acidentes)}.')
    print(f'Media de veiculos nas cinco cidades: {sum(veiculos) / len(veiculos)}.')
    print(f'Media de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {sum(acidentes_2000) / len(acidentes_2000)}')


acidentes_f()
