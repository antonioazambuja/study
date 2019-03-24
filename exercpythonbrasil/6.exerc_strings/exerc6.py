def main():
    meses = [
        'janeiro',
        'fevereiro',
        'março',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro'
    ]
    dia = int(input('informe o seu dia de nascimento: '))
    mes = int(input('informe o seu mês de nascimento: '))
    ano = int(input('informe o seu ano de nascimento: '))
    print(f'Data de Nascimento: {dia}/{mes}/{ano}.')
    print(f'Data de Nascimento: {dia} de {meses[mes-1]} de {ano}.')


main()
