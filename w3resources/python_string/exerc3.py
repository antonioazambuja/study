def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma nova string com as \
duas primeiras letras e as duas ultimas.\n---------'


def func():
    string = input('informe a string: ')
    string2 = string[:2] + string[-2:]
    [print('Cadeia vazia') if len(string) < 2 else print(string2)]
