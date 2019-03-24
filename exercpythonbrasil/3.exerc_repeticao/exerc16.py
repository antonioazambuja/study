def fibonacci_f():
    sequencia, soma = [], 0
    sequencia.append(0)
    sequencia.append(1)
    while True:
        soma = sequencia[-1] + sequencia[-2]
        if soma > 500:
            break
        else:
            sequencia.append(soma)
            continue
    print(sequencia, end=',')


fibonacci_f()
