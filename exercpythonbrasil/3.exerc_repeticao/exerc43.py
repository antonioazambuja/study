def cardapio():
    print('Especificação       Código     Preço')
    print('Cachorro Quente     100        R$ 1,20')
    print('Bauru Simples       101        R$ 1,30')
    print('Bauru com Ovo       102        R$ 1,50')
    print('Hambúrguer          103        R$ 1,20')
    print('Cheeseburguer       104        R$ 1,30')
    print('Refrigerante        105        R$ 1,00')
    tot, v_item, pedido = 0, 0, 1
    while pedido > 0:
        pedido = int(input('informe o cod do pedido: '))
        if pedido < 100 or pedido > 105:
            print('Codigo de pedido incorreto, informe novamente.')
        else:
            qtd = int(input('informe o qtd desejada: '))
            if pedido == 100:
                v_item = 1.2 * qtd
                tot += v_item
            elif pedido == 101:
                v_item = 1.3 * qtd
                tot += v_item
            elif pedido == 102:
                v_item = 1.5 * qtd
                tot += v_item
            elif pedido == 103:
                v_item = 1.2 * qtd
                tot += v_item
            elif pedido == 104:
                v_item = 1.3 * qtd
                tot += v_item
            elif pedido == 105:
                v_item = 1 * qtd
                tot += v_item
            print(f'Valor do item: R$ {round(v_item,2)}.')
            print(f'Total do pedido: R$ {round(tot,2)}')


cardapio()
