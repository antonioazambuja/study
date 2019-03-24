def main():
    notas = []
    for _ in range(0, 4):
        nota = int(input('informe a nota: '))
        notas.append(nota)
    print(notas)
    print(f'Média: {sum(notas) / len(notas)}')


main()
