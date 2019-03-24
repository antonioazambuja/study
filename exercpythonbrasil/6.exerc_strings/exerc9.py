def main():
    cont = 0
    while True:
        cpf = input('informe seu cpf: ')
        for carac in cpf:
            if carac in '0123456789':
                cont += 1
        if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-' or cont != 11:
            print('cpf inválido informe novamente.')
        else:
            print('cpf válido.')
            break
        

main()
