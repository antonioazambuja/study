def somaImposto(taxaImposto, custo):
    impostoAplic = (taxaImposto / 100) * custo
    print(f'custo com imposto aplicado: R$ {impostoAplic + custo}0.')


def main():
    taxaImposto = float(input('informe a taxa de imposto(em %): '))
    custo = float(input('informe o custo do produto: R$ '))
    somaImposto(taxaImposto, custo)


main()
