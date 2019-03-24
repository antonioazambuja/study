def main():
    caracs = []
    for _ in range(0, 10):
        carac = input('informe o caracter: ')
        if carac.upper() not in 'AEIOU':
            caracs.append(carac)
    print(f'Números de consoantes: {len(caracs)}.')
    print('Consoantes:', end=' ')
    for carac in caracs:
        print(carac,end=' ')


main()
