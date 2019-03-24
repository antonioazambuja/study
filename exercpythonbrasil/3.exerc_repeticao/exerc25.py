def idade():
    idade, soma, media = 0, 0, 0
    limite = int(input('informe o numero de pessoas: '))
    for i in range(0, limite + 1):
         idade = int(input(f'informe a idade da {i} pessoa: '))
         soma += idade
    else:
        media = soma / limite
        if 0 <= media <= 25:
            print('A maioria das pessoas são Jovens!')
        elif 26 <= media <= 60:
            print('A maioria das pessoas são Adultas!')
        elif media > 60:
            print('A maioria das pessoas são Idosas!')


idade()
