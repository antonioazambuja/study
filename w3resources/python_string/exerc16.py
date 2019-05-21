def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma nova string \
inserindo o segundo parametro no meio da primeira string.\n---------'


def insert_string_middle(string, str_mid):
    string = list(string)
    string.insert(len(string) // 2, str_mid)
    return ''.join(string)


def func():
    string_mod = input('informe a string para modif: ')
    string_insert = input('informe a string inserida: ')
    print(insert_string_middle(string_mod, string_insert))
