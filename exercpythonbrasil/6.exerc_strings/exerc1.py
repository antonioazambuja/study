def main():
    entrada_1 = input('informe a primeira frase ou palavra: ')
    entrada_2 = input('informe a segunda frase ou palavra: ')
    # retirando espaços das strings para ser contabilizado o seu comprimento
    entrada_1_esp = entrada_1.replace(' ','')
    entrada_2_esp = entrada_2.replace(' ','')
    print(f'Frase 1: "{entrada_1}" tem:{len(entrada_1_esp)} de comprimeto.')
    print(f'Frase 1: "{entrada_2}" tem:{len(entrada_2_esp)} de comprimeto.')
    # testando se os tamanhos da strings são iguais
    if len(entrada_1_esp) == len(entrada_2_esp):
        print('Frases tem o mesmo tamanho!')
    else:
        print('Frases não tem o mesmo tamanho!')
    # testando se o conteúdo das strings são os mesmos
    if entrada_1_esp == entrada_2_esp:
        print('Frases tem o mesmo conteúdo!')
    else:
        print('Frases não tem o mesmo conteúdo!')


main()    
