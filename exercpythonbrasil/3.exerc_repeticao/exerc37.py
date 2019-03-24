def academia_f():
    cliente_cod, cliente_peso, cliente_altura = 0, 0, 0
    peso, altura, cliente = [], [], []
    print('----------- Academia -----------')
    while True:
        cliente_cod = int(input('\ninforme o codigo do cliente: '))
        if cliente_cod == 0:
            break
        else:
            cliente.append(cliente_cod)
            cliente_peso = float(input('informe o peso do cliente: '))
            peso.append(cliente_peso)
            cliente_altura = float(input('informe a altura do cliente: '))
            altura.append(cliente_altura)
    # indices dos devidos clientes
    i_pesomax = peso.index(max(peso))
    i_pesomin = peso.index(min(peso))
    i_altmax = altura.index(max(altura))
    i_altmin = altura.index(min(altura))
    print(f'\nCod cliente maior peso: {cliente[i_pesomax]}. Peso: {max(peso)} kg.')
    print(f'Cod cliente menor peso: {cliente[i_pesomin]}. Peso: {min(peso)} kg.')
    print(f'Cod cliente maior altura: {cliente[i_altmax]}. Altura: {max(altura)} m.')
    print(f'Cod cliente menor altura: {cliente[i_altmin]}. Altura: {min(altura)} m.')
    print(f'Média das alturas dos clientes: {sum(altura) / len(cliente)} m')
    print(f'Média dos pesos dos clientes: {sum(peso) / len(cliente)} kg')
    

academia_f()
