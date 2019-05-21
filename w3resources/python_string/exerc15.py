def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma tag \
HTML com a string e tag informada.\n---------'


def add_tag(tag, string):
    return f'<{tag}> {string} </ {tag}>'


def func():
    tag = input('informe a tag: ')
    string = input('informe a string: ')
    print(add_tag(tag, string))
