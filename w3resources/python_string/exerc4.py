def desc():
    return f'---------\nExecutando {__name__}.\nFunção solicita uma string e um caracter, e \
retorna uma string modificando a segunda ocorrência do caracter por "$".\n---------'


def func():
    carac = input('informe um caracter: ')
    string = input('informe a string: ')
    cont = 0
    # print(string)
    for i in range(len(string)):
        if carac == string[i]:
            cont += 1
        if cont == 2:
            string = list(string)
            string[i] = '$'
            string = ''.join(string)
            break
    print(string)
