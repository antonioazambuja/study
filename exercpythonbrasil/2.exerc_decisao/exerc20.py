'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
# media, nota1, nota2, nota3 = 0, 0, 0, 0
nota1 = float(input("DIGITE A NOTA 1 DO ALUNO: "))
nota2 = float(input("DIGITE A NOTA 2 DO ALUNO: "))
nota3 = float(input("DIGITE A NOTA 3 DO ALUNO: "))
media = (nota1 + nota2 + nota3) / 3
if media == 10:
    print("APROVADO COM DISTINÇÃO! MÉDIA OBTIDA:",media)
elif media >= 7:
    print("APROVADO! MÉDIA OBTIDA:",media)
elif media < 7:
    print("REPROVADO! MÉDIA OBTIDA:",media)
