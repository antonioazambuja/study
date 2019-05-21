def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna se a string \
for maior ou igual a três os três primeiros caracteres, se não a \
string completa.\n---------'


def first_three(string):
    return string[:3] if len(string) >= 3 else string


def func():
    string = input('informe a string: ')
    print(first_three(string))
