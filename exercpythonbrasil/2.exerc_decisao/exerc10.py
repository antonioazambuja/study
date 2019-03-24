def main():
    print('informe - M - para Manhã \n          V - para Tarde \n          N - para Noite')
    while True:          
        turno = input("digite seu turno: ").upper()
        if turno == 'M' or turno == 'V' or turno == 'N':
            if turno == 'M':
                print("Bom Dia!")
            elif turno == 'V':
                print("Boa Tarde!")
            elif turno == 'N':
                print("Boa Noite!")
            break
        else:
            print('Turno inválido, informe novamente.')


main()
