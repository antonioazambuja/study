def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma nova string invertendo a \
primeira letra pela última.\n---------'


def func():
    string = input('informe a string: ')
    string = list(string)
    aux_inicio = string[0]
    aux_fim = string[-1]
    string[0] = aux_fim
    string[-1] = aux_inicio
    print(''.join(string))
