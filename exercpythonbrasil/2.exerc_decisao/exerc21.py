'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.
'''

saque = float(input("INFORME O VALOR DO SAQUE: "))
if saque > 0:
    saque_final = saque
    nota100 = saque_final // 100
    saque_final = saque % 100
    nota50 = saque_final // 50
    saque_final = saque % 50
    nota10 = saque_final // 10
    saque_final = saque % 10
    nota5 = saque_final // 5
    saque_final = saque % 5
    nota1 = saque_final // 1
    saque_final = saque % 1
    print("NOTAS DE 100:",nota100,", NOTAS DE 50:",nota50,", NOTAS DE 10:",nota10,", NOTAS DE 5:",nota5,"NOTAS DE 1:",nota1,'.')
else:
    print("VALOR INVÁLIDO!")
