def tabuada_f():
    num = int(input('informe a tabuada de qual numero deseja realizar: '))
    num_origem = int(input('informe a origem da tabuada: '))
    num_limite = int(input('informe o limite da tabuada: '))
    print(f'Montarei a tabuada do {num} do {num_origem} até {num_limite}.')
    for num2 in range(num_origem, num_limite + 1):
        print(f'\n{num} X {num2} = {num * num2}')


tabuada_f()
