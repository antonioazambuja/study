# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []
for _ in range(4):
    lista.append(int(input('informe o numero: ')))
else:
    print(f'Notas:', end= ' ')
    for carac in lista:
        print(carac, end=' ')
    print(f'\nMédia: {sum(lista) / len(lista)}')
