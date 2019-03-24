def main():
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezenas = ['zero', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    unidade_dez = ['zero', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    while True:
        num = input('informe o numero entre 1 e 99: ')
        if 1 > int(num) > 99:
            print('numero fora do range, informe um numero entre 1 e 99.')
        else:
            if len(num) == 1:
                print(f'numero por extenso: {unidades[int(num[0])]}')
            elif len(num) == 2:
                if num[0] == '1':
                    print(f'numero por extenso: {unidade_dez[int(num[1])]}')
                else:
                    print(f'numero por extenso: {dezenas[int(num[0])]} e {unidades[int(num[1])]}.')
            break


main()
