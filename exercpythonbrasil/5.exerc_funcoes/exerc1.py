def main():
    num = int(input('informe o limite: '))
    for i in range(1, num + 1):
        for _ in range(0, i):
            print(i, end = ' ')
        print ('\n')


main()
