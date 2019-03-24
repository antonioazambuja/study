def main():
    frase = input('informe a frase: ')
    frase = frase.replace(' ', '')
    if frase == frase[::-1]:
        print('palavra palíndroma!')
    else:
        print('palavra não palíndroma!')
    

main()
