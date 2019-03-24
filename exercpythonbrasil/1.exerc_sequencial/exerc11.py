"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A. o produto do dobro do primeiro com metade do segundo .
B. a soma do triplo do primeiro com o terceiro.
C. o terceiro elevado ao cubo.
"""
num = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

# A.
a = (num * 2) * (num2/2)
print("o produto do dobro do primeiro com metade do segundo:",a)

# B.
b = (num * 3) + num3
print("a soma do triplo do primeiro com o terceiro:",b)

# C.
c = num3 ** 2
print("o terceiro elevado ao cubo:",c)
