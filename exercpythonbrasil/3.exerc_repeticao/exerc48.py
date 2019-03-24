numero, cont25, cont50, cont75, cont100 = 0, 0, 0, 0, 0
while numero <= 0:
    numero = int(input("digite o numero: "))
    if 0 <= numero <= 25:
        cont25 += 1
    elif 26 <= numero <= 50:
        cont50 += 1
    elif 51 <= numero <= 75:
        cont75 += 1
    elif 76 <= numero <= 100:
        cont100 += 1
    else:
        print('Numero invalido!')
print(f'Contagens:\n0 a 25: {cont25}\n26 a 50: {cont50}\n51 a 75: {cont75}\n76 a 100: {cont100}')
