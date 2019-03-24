def maior_f():
    numeros = []
    for _ in range(0, 5):
        num = int(input('informe o numero: '))
        numeros.append(num)
    cont = numeros.count(num)
    if cont == 5:
        print(f'Numeros iguais: {num}.')
    else:
        print(f'Maior número é: {max(numeros)}.')


maior_f()
