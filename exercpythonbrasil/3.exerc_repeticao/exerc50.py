def calculo_f():
    h = 0
    limite = int(input('informe o numero de termos: '))
    for num in range(1, limite + 1):
        h += (1 / num)
    print(f'Resultado H: {h}.')


calculo_f()
