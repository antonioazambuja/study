def habitantes_f():
    A, B, cont = 80000, 200000, 0
    while A < B:
        A += A * 0.3
        B += B * 0.15
        cont += 1
    else:
        print(f'Anos necessários para que a população de A ultrapasse ou se iguale a população de B: {cont} anos.')


habitantes_f()
