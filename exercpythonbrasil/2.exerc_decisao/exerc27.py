'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
'''
def main():
    morango = int(input("kgs de morangos: "))
    maca = int(input("kgs de maças: "))
    if morango <= 5:
        preco_morango = 2.5 * morango
    else:
        preco_morango = 2.2 * morango
    if maca <= 5:
        preco_maca = 1.8 * maca
    else:
        preco_maca = 1.5 * maca
    preco_final = preco_maca + preco_morango
    peso_total = morango + maca
    if peso_total > 8 or preco_final > 25:
        preco_final -= preco_final * 0.1
    print('R$: ',preco_final)


main()
