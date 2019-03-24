def main():
    # salario_novo = 0
    salario = float(input("digite o salario: R$ "))
    if salario <= 280.0:
        porcent = 0.20
        percent = salario * porcent
        salario_novo = salario + percent
    elif salario > 280.0 and salario <= 700.0:
        porcent = 0.15
        percent = salario * porcent
        salario_novo = salario + percent
    elif salario > 700.0 and salario <= 1500.0:
        porcent = 0.10
        percent = salario * porcent
        salario_novo = salario + percent
    elif salario > 1500.0:
        porcent = 0.05
        percent = salario * porcent
        salario_novo = salario + percent
    print("salario: R$", salario)
    print(f"percentual aumentado: {int(porcent*100)}%")
    print("valor aumentado: R$", percent)
    print("novo salario: R$", salario_novo)


main()
