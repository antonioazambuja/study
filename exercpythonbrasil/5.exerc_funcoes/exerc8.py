def numeroDig(num):
    num = str(num)
    return len(num)


def main():
    num = int(input('informe o numero: '))
    print(f'O numero de digitos do numero é {numeroDig(num)}.')


main()
