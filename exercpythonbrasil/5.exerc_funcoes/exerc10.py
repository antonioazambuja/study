from random import randint


def crapsJogo():
    print('VOCÊ ESTÁ JOGANDO CRAPS!\n')
    while True:
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        result = dado1 + dado2
        if result == 7 or result == 11:
            print('NATURAL, VOCÊ GANHOU!')
            break
        elif result == 2 or result == 3 or result == 12:
            print('CRAPS, VOCÊ PERDEU!')
            break
        elif str(result) in '4568910':
            ponto = result
            input(f'VOCÊ TIROU {result} ESSE É SEU "PONTO", PRESSIONE QUALQUER TECLA PARA CONTINUAR...')
            while True:
                dado1 = randint(1,6)
                dado2 = randint(1,6)
                result = dado1 + dado2
                if result == 7:
                    print('VOCÊ TIROU 7 ANTES DE TIRAR SEU "PONTO", VOCÊ PERDEU!')
                    break
                elif result == ponto:
                    print('VOCÊ TIROU SUE PONTO E GANHOU')
                    break
            break


def main():
    crapsJogo()


main()
