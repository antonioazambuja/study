def main():
    nome = input('informe o seu nome: ').upper()
    for i in range(1, len(nome) + 1):
        print(nome[:i])
    

main()
