def numeros_f():
    limite = int(input('informe o limite de numeros da serie: '))
    lista = []
    for _ in range(0, limite):
        while True:
            num = int(input('informe o numero: '))
            if num < 1 or num > 1000:
                print('Numero fora do range, informe número entre 1 e 1000.')
            else:
                lista.append(num)
                break
    else:
        cont = lista.count(num)
        if cont == len(lista):
            print(f'Numeros Iguais!')
            print(f'Soma: {sum(lista)}, Maior numero: {max(lista)} e Menor numero: {min(lista)}.')
        else:
            print(f'Soma: {sum(lista)}, Maior numero: {max(lista)} e Menor numero: {min(lista)}.')


numeros_f()
