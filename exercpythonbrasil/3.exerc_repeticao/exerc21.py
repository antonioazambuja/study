def primo_f():
    cont = 0
    num = int(input('digite o numero: '))
    for div in range(1, num+1):
        if num % div == 0:
            cont += 1
    if cont == 2:
        print(f'Numero {num} é primo!')
    else:
        print('Não é primo!')


primo_f()
