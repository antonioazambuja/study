def primos():
    lista, cont_div = [], 0
    limite = int(input("digite o numero: "))
    for num in range(limite - 1, 0, -1):
        limite2, cont = num, 0
        for div in range(limite2, 0, -1):
            if num % div == 0:
                cont += 1
        else:
            if cont == 2:
                lista.append(num)
            cont_div += cont
    else:
        print(lista)
        print(f'num divisoes: {cont_div}.')


primos()
