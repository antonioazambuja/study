def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma nova string \
removendo o caracter do parametro "indíce - 1".\n---------'


def func():
    string = input('informe a string: ')
    index = int(input('informe o indíce: '))
    string_mod = list(string)
    string_mod[index - 1] = ''
    string_mod = ''.join(string_mod)
    print(string_mod)
