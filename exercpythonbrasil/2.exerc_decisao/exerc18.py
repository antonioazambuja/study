dia = int(input("digite o dia da data: "))
mes = int(input("digite o mês da data: "))
ano = int(input("digite o ano da data: "))
if ano % 4 == 0:
    if mes == 2:
        if dia > 0 and dia <= 29:
            print("Data Válida!")
        else:
            print("Data Inválida!")
elif ano > 0:
    if mes == 2:
        if dia > 0 and dia <= 28:
            print("Data Válida!")
        else:
            print("Data Inválida!")
    elif mes > 0 and mes <= 12:
        if dia > 0 and dia < 31:
            print("Data Válida!")
        else:
            print("Data Inválida!")
    else:
        print("Data Inválida!")
