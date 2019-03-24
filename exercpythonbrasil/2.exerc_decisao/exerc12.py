ir = 0
inss = 0
fgts = 0
tot_desc = 0
salario_liq = 0
salario = 0

valor_hora = float(input("digite a o valor da sua hora de trabalho: "))
qtd_hora = int(input("digite a qtd de horas trabalhadas: "))
salario = valor_hora * qtd_hora
if salario <= 900:
    fgts = salario * 0.11
    print("Salário Bruto           : R$", salario)
    print("(-) IR (0%)             : R$", ir)
    print("(-) INSS (0%)           : R$", inss)
    print("FGTS (11%)              : R$", fgts)
    tot_desc = ir + inss
    print("Total de descontos      : R$", tot_desc)
    salario_liq = salario - tot_desc
    print("Salário Liquido         : R$", salario_liq)
elif salario <= 1500:
    ir = salario * 0.05
    fgts = salario * 0.11
    inss = salario * 0.1
    print("Salário Bruto           : R$", salario)
    print("(-) IR (5%)             : R$", ir)
    print("(-) INSS (10%)          : R$", inss)
    print("FGTS (11%)              : R$", fgts)
    tot_desc = ir + inss
    print("Total de descontos      : R$", tot_desc)
    salario_liq = salario - tot_desc
    print("Salário Liquido         : R$", salario_liq)
elif salario <= 2500:
    ir = salario * 0.1
    fgts = salario * 0.11
    inss = salario * 0.1
    print("Salário Bruto           : R$", salario)
    print("(-) IR (10%)            : R$", ir)
    print("(-) INSS (10%)          : R$", inss)
    print("FGTS (11%)              : R$", fgts)
    tot_desc = ir + inss
    print("Total de descontos      : R$", tot_desc)
    salario_liq = salario - tot_desc
    print("Salário Liquido         : R$", salario_liq)
elif salario > 2500:
    ir = salario * 0.2
    fgts = salario * 0.11
    inss = salario * 0.1
    print("Salário Bruto           : R$", salario)
    print("(-) IR (20%)            : R$", ir)
    print("(-) INSS (10%)          : R$", inss)
    print("FGTS (11%)              : R$", fgts)
    tot_desc = ir + inss
    print("Total de descontos      : R$", tot_desc)
    salario_liq = salario - tot_desc
    print("Salário Liquido         : R$", salario_liq)
    