def primo_f():
    cont, lista = 0, []
    num = int(input('digite o numero: '))
    for div in range(1, num+1):
        if num % div == 0:
            cont += 1
            lista.append(div)
    if cont == 2:
        print(f'Numero {num} é primo!')
    else:
        print('Não é primo!')
        print(f'Divisivel por: {lista}.')


primo_f()
