def desc():
    return f'---------\nExecutando {__name__}.\nFunção verifica a qtd de ocorrências \
de cada palavra na frase.\n---------'


def func():
    frase = input('informe a string: ')
    frase = frase.split()
    dicio = {}
    for i in range(len(frase)):
        if frase[i] not in dicio.keys():
            dicio[frase[i]] = frase.count(frase[i])
    for k, v in dicio.items():
        print(k, ' - ', v)
