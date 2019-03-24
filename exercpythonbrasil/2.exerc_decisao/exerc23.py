'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
'''
numero = float(input("digite o numero: "))
num = int(str(round(numero, 2))[-1])
if num == 0:
    print("inteiro")
else:
    print("decimal")
