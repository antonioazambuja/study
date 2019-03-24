def valor_final_f():
    soma, cont, valor = 0, 0, 1
    while valor > 0:
        valor = int(input("informe o valor do produto: R$ "))
        cont = cont + 1
        soma += valor
        print(f'Produto {cont}: R$ {valor}.\n')
    else:
        print(f'Valor total é: {soma}')
        return soma


def main():
    print('Lojas Tabajara\n')
    valor_tot = valor_final_f()
    pagamento = int(input("informe o pagamento: R$ "))
    troco = pagamento - valor_tot
    while troco < 0:
        print('Valor insuficiente!')
        pagamento = int(input("informe o pagamento novamente: R$ "))
        troco = pagamento - valor_tot
    if troco > 0:
        print(f'Troco de R$ {troco}')
    else:
        print('Pagamento efetuado!')


main()
