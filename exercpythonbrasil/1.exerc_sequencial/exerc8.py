""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
valor_hora = float(input("Informe o valor da hora trabalhada: "))
horas_trabalhadas = int(input("Informe o numero de horas trabalhadas: "))
print(f'O seu salário é: R${int(horas_trabalhadas * valor_hora)}.')
