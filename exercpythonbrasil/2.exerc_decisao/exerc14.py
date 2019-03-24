def main():
    n1 = float(input('informe a nota: '))
    n2 = float(input('informe a nota: '))
    media = (n1 + n2) / 2
    if media >= 0 and media <= 4:
        conceito = 'E'
    elif media > 4 and media <= 6:
        conceito = 'D'
    elif media > 6 and media <= 7.5:
        conceito = 'C'
    elif media > 7.5 and media <= 9:
        conceito = 'B'
    elif media > 9 and media <= 10:
        conceito = 'A'
    print(f'Conceito obtido: {conceito}.')
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        print('Aprovado!')
    else:
        print('Reprovado.')


main()
