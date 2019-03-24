def votos():
    voto, votos = 0, []
    num_cand = int(input('informe o numero de candidatos: '))
    for _ in range(1, num_cand + 1):
        while True:
            voto = int(input('informe o seu voto: '))
            if voto < 1 or voto > 3:
                print('Voto inválido, vote novamente.')
            else:
                votos.append(voto)
                break
    else:
        print(f'\nCandidato 1: {votos.count(1)} votos.')
        print(f'Candidato 2: {votos.count(2)} votos.')
        print(f'Candidato 3: {votos.count(3)} votos.')


votos()
