def desc():
    return f'---------\nExecutando {__name__}.\nFunção retorna uma string trocando entre si \
o segundo elemento de cada palavra.\n---------'


def func():
    while True:
        str_comp = input('informe a string: ')
        str_list = str_comp.split()
        if len(str_list) < 2:
            print('informe novamente!')
        else:
            str1 = str_list[0]
            str1_aux = str1[:2]

            str2 = str_list[1]
            str2_aux = str2[:2]

            str1 = str1.replace(str1_aux, str2_aux)
            str2 = str2.replace(str2_aux, str1_aux)
            print(str1, str2)
            break
