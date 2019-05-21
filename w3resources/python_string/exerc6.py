def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma nova string atribuindo "ing" \
a todas as palavras, se já for "ing", atribui "ly".\n---------'


def func():
    string = input('informe a string: ')
    if len(string) >= 3:
        if string[-3:] != 'ing':
            string += 'ing'
        else:
            string += 'ly'
    print(string)
