def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma nova string \
removendo todos os indíces ímpares.\n---------'


def func():
    string = input('informe a string: ')
    string = list(string)
    for i in range(len(string)):
        if i % 2 != 0:
            string[i] = ''
    print(''.join(string))
