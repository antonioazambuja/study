def numeros_f():
    limite = int(input('informe o limite de numeros da serie: '))
    numeros = []
    for _ in range(0, limite):
        num = int(input('informe o numero: '))
        numeros.append(num)
    print(f'Soma: {sum(numeros)}, Maior numero: {max(numeros)} e Menor numero: {min(numeros)}.')


numeros_f()
