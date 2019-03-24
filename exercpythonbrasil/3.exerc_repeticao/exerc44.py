def eleicao_f():
    sair, voto, votos = 1, 0, []
    print('''1, 2, 3, 4 - Votos para os respectivos candidatos:
1 - Candidato 1
2 - Candidato 2
3 - Candidato 3
4 - Candidato 4
5 - Voto Nulo
6 - Voto em Branco''')
    while sair == 1:
        while True:
            voto = int(input("digite o numero correspondente ao seu candidato: "))
            if voto < 1 or voto > 6:
                print('Voto inválido!')
            else:
                votos.append(voto)
                break
        sair = int(input("Deseja sair ou continuar? (0 - Sair e 1 - Continuar) "))
    else:
        print(f'Candidato 1: {votos.count(1)} / Candidato 2: {votos.count(2)}')
        print(f'Candidato 3: {votos.count(3)} / Candidato 4: {votos.count(4)}')
        print(f'Votos Nulo: {votos.count(5)} / Votos em Branco: {votos.count(6)}')
        print(f'Percentual de Votos Nulos sobre o total de votos: {round(votos.count(5) / sum(votos) * 100,2)}%')
        print(f'Percentual de Votos em Branco sobre o total de votos: {round(votos.count(6) / sum(votos) * 100,2)}%')


eleicao_f()
