nota_1 = float(input("digite a nota: "))
nota_2 = float(input("digite a nota: "))
nota_f = (nota_1 + nota_2) / 2
if nota_f == 10.0:
    print("aprovado com distinção!")
elif nota_f >= 7:
    print("aprovado!")
else:
    print("reprovado!")
