# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
for _ in range(10):
    lista.append(int(input('informe o numero: ')))
else:
    lista.sort(reverse=True)
    print(lista)
