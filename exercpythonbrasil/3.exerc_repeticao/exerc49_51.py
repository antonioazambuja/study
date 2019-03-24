def serie_f():
    soma, result = 0, 0
    n = int(input('informe n: '))
    m = int(input('informe m: '))
    while n != 0 and m != 0:
        soma += n / m
        m -= 2
        n -= 1
    print(f'Soma da série: {soma}')


serie_f()
