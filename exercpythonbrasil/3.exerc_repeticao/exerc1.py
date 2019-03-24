def main():
    while True:
        nota = float(input("digite uma nota: "))
        if nota < 0 or nota > 10:
            print("nota invalida, informe novamente.")
        else:
            print("nota válida!") 


main()
