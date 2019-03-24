def main():
    num = int(input('informe o limite: '))
    for i in range(1, num + 1):
        for i2 in range(1, i + 1):
            print(i2, end = ' ')
        print('\n')


main()
