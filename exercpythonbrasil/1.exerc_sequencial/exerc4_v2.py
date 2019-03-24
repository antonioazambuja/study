def media(notas):
    media = (sum(notas) / len(notas))
    print(media)


def main():
    notas, nota, limite = [], 0, 0
    limite = int(input('informe o número de notas: '))
    for _ in range(limite):
        nota = int(input('informe a nota: '))
        notas.append(nota)
    media(notas)


main()