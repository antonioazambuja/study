main()
    produtos = []
    for _ in range(3):
        produto = float(input('informe o valor do produto: '))
        produtos.append(produto)
    print(f'Compre o produto: R${min(produtos)}.')


main()
