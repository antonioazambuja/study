def notas_f():
    sair, cont, nota, nota_turma = 1, 0, 0, 0
    while sair == 1:
        cont += 1
        q1 = input('informe a resposta da questão 01: ').upper()
        if q1 == 'A':
            nota += 1
        q2 = input('informe a resposta da questão 02: ').upper()
        if q2 == 'B':
            nota += 1
        q3 = input('informe a resposta da questão 03: ').upper()
        if q3 == 'C':
            nota += 1
        q4 = input('informe a resposta da questão 04: ').upper()
        if q4 == 'D':
            nota += 1
        q5 = input('informe a resposta da questão 05: ').upper()
        if q5 == 'E':
            nota += 1
        q6 = input('informe a resposta da questão 06: ').upper()
        if q6 == 'E':
            nota += 1
        q7 = input('informe a resposta da questão 07: ').upper()
        if q7 == 'D':
            nota += 1
        q8 = input('informe a resposta da questão 08: ').upper()
        if q8 == 'C':
            nota += 1
        q9 = input('informe a resposta da questão 09: ').upper()
        if q9 == 'B':
            nota += 1
        q10 = input('informe a resposta da questão 10: ').upper()
        if q10 == 'A':
            nota += 1
        nota_turma += nota
        sair = int(input("Deseja continuar? (SIM - 1 ou NÃO - 0) "))
    print('Media da Turma:',nota_turma / cont,'pts.')


notas_f()