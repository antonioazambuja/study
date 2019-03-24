def main():
    while True:
        sexo = input("Digite o Sexo: ")
        if sexo == 'M' or sexo == 'm':
            print("M - Masculino")
            break
        elif sexo == 'F' or sexo == 'f':
            print("F - Feminino")
            break
        else:
            print('Informe um sexo válido.')


main()
