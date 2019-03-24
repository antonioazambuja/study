def main():
    print('Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:')
    print('a. quantos espaços em branco existem na frase.')
    print('b. quantas vezes aparecem as vogais a, e, i, o, u.\n')
    cont_esp, cont_vog = 0, 0
    frase = input('informe a frase ou palavra: ')
    for carac in frase:
        if carac == ' ':
            cont_esp += 1
        elif carac in 'aeiou':
            cont_vog += 1
    print(f'Contagem de espaços: {cont_esp}')
    print(f'Contagem de vogais: {cont_vog}')


main()
