def exp_f():
    result = 1
    base = int(input('informe a base do calculo: '))
    expoente = int(input('informe o expoente: '))
    for _ in range(1, expoente + 1):
        result *= base
    print(f'Resultado: {result}')


exp_f()
