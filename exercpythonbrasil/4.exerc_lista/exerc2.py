def main():
    numeros = []
    for _ in range(0, 10):
        num = int(input('informe o numero: '))
        numeros.append(num)
    numeros.sort(reverse=True)
    print(numeros)

main()
