def numero():
    cont_p, cont_i = 0, 0
    for _ in range(0, 10):
        num = int(input(f"informe o numero: "))
        if num % 2 == 0:
            cont_p += 1
        else:
            cont_i += 1
    else:
        print(f'Numeros pares: {cont_p} e Numeros impares: {cont_i}')


numero()
