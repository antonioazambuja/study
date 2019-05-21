def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna a \
string sem ", ".\n---------'


def func():
    frase = input('informe as palavras separadas por ", ": ')
    frase_list = frase.split(', ')
    frase_list.sort()
    print(' '.join(frase_list))
