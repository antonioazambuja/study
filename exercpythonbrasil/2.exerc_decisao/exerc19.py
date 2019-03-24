"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades.
12 = 1 dezena e 2 unidades.
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.
"""
centena = 0
dezena = 0
unid =0
numero = []
numero = int(input("digite um numero:"))
if numero < 1000:
    centena = int(str(numero // 100)[-1])
    dezena  = int(str(numero // 10)[-1])
    unid = int(str(numero)[-1])
    if centena > 1:
        p_centena = 'centenas'
    else:
        p_centena = 'centena'
    if dezena > 1:
        p_dezena = 'dezenas'
    else:
        p_dezena = 'dezena'
    if unid > 1:
        p_unid = 'unidades'
    else:
        p_unid = 'unidade'
    print(numero,'=',centena,p_centena,',',dezena,p_dezena,'e',unid,p_unid,'.')
else:
    print("Número inválido!")
