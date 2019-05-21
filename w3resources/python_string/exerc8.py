def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna a maior string da \
frase.\n---------'


def func():
    string = input('informe a string: ')
    string_list = string.split()
    print(max(string_list, key=len))
