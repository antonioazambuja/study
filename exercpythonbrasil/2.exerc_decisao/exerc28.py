'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''
def main():
    while True:
        tipo = input("informe qual a carne ira ser comprada(F-filé duplo, A-Alcatra e P-Picanha): ").upper()
        if tipo != 'F' and tipo != 'P' and tipo != 'A':
            print('tipo de carne inválida, informe novamente.')
        else:
            break
    pagamento = input("pagamento com cartao(C-Cartão e D-Dinheiro): ").upper()
    if tipo == 'F':
        file_duplo = int(input("qtd de file: "))
        if file_duplo <= 5:
            preco = 4.9 * file_duplo
        else:
            preco = 5.8 * file_duplo
        tipo = 'Filé Duplo'
        if pagamento == 'C':
            desc = preco * 0.05
            preco_final = preco - desc
        print(f'{tipo}.')
        print('Qtd:',file_duplo,'Kg')
    elif tipo == 'A':
        alcatra = int(input("qtd de alcatra: "))
        if alcatra <= 5:
            preco = 5.9 * alcatra
        else:
            preco = 6.8 * alcatra
        tipo = 'Alcatra'
        if pagamento == 'C':
            desc = preco * 0.05
            preco_final = preco - desc
        print(f'{tipo}.')
        print('Qtd:',alcatra,'Kg')
    elif tipo == 'P':
        picanha = int(input("qtd de picanha: "))
        if picanha <= 5:
            preco = 6.9 * picanha
        else:
            preco = 7.8 * picanha
        tipo = 'Picanha'
        if pagamento == 'C':
            desc = preco * 0.05
            preco_final = preco - desc
        print(f'{tipo}.')
        print('Qtd:',picanha)
    print('Valor Total: R$',preco)
    print('Cartão ou Dinheiro:'+ (' Cartão.'if pagamento == 'C' else ' Dinheiro.'))
    print('Desconto: R$',desc)
    print('Valor a pagar: R$',preco_final)


main()
