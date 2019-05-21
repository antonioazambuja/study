def desc():
    return f'---------\nExecutando {__name__}.\nFunção verifica se a string é maior \
ou igual que a 2, e então repete os dois ultimos caracteres 4x.\n---------'


def insert_end(string):
    if len(string) >= 2:
        str_copy = string[-2:]
        return str_copy * 4


def func():
    string = input('informe a string: ')
    print(insert_end(string))
