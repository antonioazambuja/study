def fatorial_f():
    num = int(input('informe o numero: '))
    for i in range(1, num):
        num *= i
    print(f'Resultado: {num}.')  


fatorial_f()
