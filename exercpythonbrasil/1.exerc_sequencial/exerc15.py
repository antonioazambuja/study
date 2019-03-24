"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
A. salário bruto.
B. quanto pagou ao INSS.
C. quanto pagou ao sindicato.
D. o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
"""
valor_hora = float(input("Informe o valor da hora: "))
horas_trabalhadas = float(input("Informe as horas trabalhadas: "))
salario_bruto = valor_hora * horas_trabalhadas
print("Salário Bruto: R$",salario_bruto)
IR = salario_bruto * 0.11
#IR = salario_bruto - IR
print("Imposto de Renda (11%): R$",IR)
INSS = salario_bruto * 0.08
#INSS = salario_bruto - INSS
print("INSS (8%): R$",INSS)
sindicato = salario_bruto * 0.05
#sindicato = salario_bruto - sindicato
print("Sindicato (5%): R$",sindicato)
salario_liquido = salario_bruto - sindicato - INSS - IR
print("Salário Liquido: R$",salario_liquido)
