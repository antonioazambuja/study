def desc():
    return f'---------\nExecutando {__name__}.\nRetorna a qtd de letras \
ordenadas por ocorrência.\n---------'


def func():
    string = input('informe a string: ')
    dicion = {carac: string.count(carac) for carac in string}
    print({k: dicion[k] for k in sorted(dicion, key=dicion.get, reverse=True)})
