def main():
    a = float(input("digite o valor da raiz A:"))
    if a == 0:
        print("a equação não é do segundo grau!")
    else:
        b = float(input("digite o valor da raiz B:"))
        c = float(input("digite o valor da raiz C:"))
        # delta da equação quadrada
        delta = b ** 2 - 4 * a * c
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        if delta < 0:
            print("a equação não possui raízes reais!")
        elif delta == 0:
            print("Conjunto Solução: {",x1,",",x2,"}")
            print("raizes são iguais pois o delta é 0!")
        elif delta > 0:
            print("Conjunto Solução: {",x1,",",x2,"}")


main()
