def saltos():
    while True:
        salto, media_salto = [], 0
        atleta = input('informe o nome do atleta: ')
        if atleta == '':
            break
        while len(salto) < 5:
            salto.append(float(input('informe o primeiro salto: ')))
        else:
            media_salto = (max(salto) - min(salto)) / (len(salto) - 2)
            print(f'Atleta: {atleta}')
            print(f'\nPrimeiro Salto: {salto[0]} m.')
            print(f'Segundo Salto: {salto[1]} m.')
            print(f'Terceiro Salto: {salto[2]} m.')
            print(f'Quarto Salto: {salto[3]} m.')
            print(f'Quinto Salto: {salto[4]} m.')
            print(f'\nMelhor salto: {max(salto)} m.')
            print(f'Pior salto: {min(salto)} m.')
            print(f'Média dos demais saltos: {round(media_salto,2)} m.')
            print(f'\nResultado Final:')
            print(f'{atleta}: {round(media_salto,2)} m.')


saltos()
