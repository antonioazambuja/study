'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
def main():
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite um numero: "))
    while True:
        op = input("escolha o operação desejada (soma: '+', subtração: '-', divisão: '/' e mutiplicação: '*'): ")
        if op == '+':
            numero = num1 + num2
            break
        elif op == '-':
            numero = num1 - num2
            break
        elif op == '/':
            numero = num1 / num2
            break
        elif op == '*':
            numero = num1 * num2
            break
        else:
            print('função inválida informe novamente.')
    if numero % 2 == 0:
        print('Número é Par', end=',')
    else:
        print('Número é Ímpar', end=',')
    if numero < 0:
        print(' Negativo', end=' e')
    else:
        print(' Positivo', end=' e')
    if numero // 1 == numero:
        print(' Inteiro.')
    else:
        print(' Decimal.')


main()
