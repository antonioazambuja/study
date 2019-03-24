def main():
    user = 0
    senha = 0
    while True:
        user = input("digite seu usuário: ")
        senha = input("digite sua senha: ")
        if senha == user:
            print("usuário e senha iguais, digite novamente.")
        else:
            print("usuário e senha cadastrados!")
            break
    print(f"Nome de Usuário: {user} e Senha: {senha}.")


main()
