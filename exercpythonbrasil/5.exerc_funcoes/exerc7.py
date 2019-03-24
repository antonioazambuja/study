def valorPagamento(valor, dias):
    if dias == 0:
        return valor
    else:
        valor += valor * 0.3
        valor += dias * 0.1
        return valor


def  main():
    cont_pag, valor_tot = 0, 0
    while True:
        valor = float(input('informe o valor da prestação: '))
        if valor == 0:
            print('programa encerrado!\n\nRelatório...')
            print(f'Qtd de pagamentos realizados hoje: {cont_pag} pagamentos.')
            print(f'Valor total pago hoje: R$ {round(valor_tot,2)}.')
            break
        else:
            dias = int(input('informe os dias em atraso da prestação: '))
            pagamento = valorPagamento(valor, dias)
            # adicionando os resultados ao relatório
            valor_tot += pagamento
            cont_pag += 1
            print(f'Valor a ser pago: R$ {pagamento}.')


main()
