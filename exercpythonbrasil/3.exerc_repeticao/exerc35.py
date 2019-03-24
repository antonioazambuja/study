def primos_f():
    limite = int(input('informe o limite de numeros primos: '))
    for num in range(1, limite+1):
        cont = 0
        for num2 in range(1, num+1):
            if num % num2 == 0:
                cont += 1
        if cont == 2:
            print(f'{num}', end=',')


primos_f()
