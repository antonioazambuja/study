def dataExt(data):
    dia, mes, ano = 0, 0, 0
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 
    'outubro', 'novembro', 'dezembro']
    if data[2] != '/' or data[5] != '/' or len(data) != 10:
        print('formato invalido!')
    else:
        dia = int(data[:2])
        mes = int(data[3:5])
        ano = int(data[6:])
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1 or ano > 2019:
        print('data inválida!')
    else:
        print(f'Data por extenso: {dia} de {meses[mes - 1]} de {ano}.')


def main():
    data = input('informe a data no formato(DD/MM/AAAA): ')
    dataExt(data)


main()
