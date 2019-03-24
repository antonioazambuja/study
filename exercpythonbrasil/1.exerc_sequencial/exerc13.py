"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
A. Para homens: (72.7*h) - 58
B. Para mulheres: (62.1*h) - 44.7
"""
altura = float(input("Informe a altura: "))
while True:
    sexo = input("H - Homem ou M - Mulher: ")
    if sexo == 'h' or sexo == 'H' or sexo == 'm' or sexo == 'M':
        break
    else:
        print('Sexo não reconhecido. Informe novamente.')
if sexo == 'h' or sexo == 'H':
    print((72.7*altura)-58)
else:
    print((62.1*altura)-44.7)
