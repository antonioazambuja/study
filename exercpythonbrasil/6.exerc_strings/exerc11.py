def main():
    from random import randint


    palavras = [
        'python',
        'ruby',
        'html',
        'css',
        'java',
        'java script',
        'php'
    ]
    letras_achadas, cont_letras, cont_tot, cont_erros = [], 0, 0, 0
    # atribuindo aleatoriamente um palavra da lista a variavel
    escolha = palavras[randint(0, 6)]
    # digitando '_' respectivamente do tamanho da palavra escolhida
    for _ in range(len(escolha)):
        print('_', end =' ')
    while True:
        letra = input('\ninforme a letra: ')
        if letra not in escolha:
            print('letra errada, digite novamente.')
            cont_erros += 1
            if cont_erros == 6:
                print('voce errou 6 vezes e foi enforcado.')
                break
        elif len(letra) > 1:
            print('informe apenas uma letra.')
        elif letra in letras_achadas:
            print('letra já encontrada informe outra.')
        else:
            # contar quantas vezes a palavra aparece na frase
            cont_letras = escolha.count(letra)
            # adicionar a lista de letras achadas a letra encontrada
            letras_achadas.append(letra)
            # adicionando a quantidade total de palvras e testando se todas foram achadas
            cont_tot += cont_letras
            if cont_tot == len(escolha):
                print('voce acertou.')
                for carac in escolha:
                    print(carac, end = ' ')
                break
            # mostrando as letras encontradas em seus respectivos lugares
            for carac in escolha:
                if carac in letras_achadas:
                    print(carac, end = ' ')
                else:
                    print('_', end = ' ')
            

main()
