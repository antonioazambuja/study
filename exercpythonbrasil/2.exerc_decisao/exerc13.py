def main():
    dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    while True:
        dia = int(input("digite o numero do dia: "))
        if dia not in range(1, 8):
            print('dia inválido, informe novamente.')
        else:
            break
    print(f'O dia corresponde há: {dias_semana[dia-1]}.')


main()
