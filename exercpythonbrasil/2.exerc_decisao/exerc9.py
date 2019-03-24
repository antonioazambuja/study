def main():
    numeros = []
    for _ in range(3):
        num = input('informe o numero: ')
        numeros.append(num)
    numeros.sort(reverse=True)
    print('Sequência decrescente:')
    for i in range(3):
        print(numeros[i], end=' ')


main()

# num_1 = int(input("digite um numero: "))
# num_2 = int(input("digite um numero: "))
# num_3 = int(input("digite um numero: "))
# # maior numero
# if num_1 > num_2 and num_1 > num_3:
#     maior_1 = num_1
# elif num_2 > num_3:
#     maior_1 = num_2
# else:
#     maior_1 = num_3
# # menor numero
# if num_1 < num_2 and num_1 < num_3:
#     maior_3 = num_1
# elif num_2 < num_3:
#     maior_3 = num_2
# else:
#     maior_3 = num_3
# # numero intermediario
# if num_1 > maior_3 and num_1 < maior_1:
#     maior_2 = num_1
# elif num_2 > maior_3 and num_2 < maior_1:
#     maior_2 = num_2
# elif num_3 > maior_3 and num_3 < maior_1:
#     maior_2 = num_3
# print("sequencia: ",maior_1, maior_2, maior_3)
