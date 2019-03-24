def inverteNum(num):
    num = str(num)
    return num[::-1]


def main():
    num = int(input('informe um numero: '))
    print(f'{num} -> {inverteNum(num)}.')


main()
