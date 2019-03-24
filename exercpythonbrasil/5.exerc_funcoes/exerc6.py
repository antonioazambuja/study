def conversao():
    while True:
        hora = int(input('informe a hora: '))
        if hora < 0 or hora > 24:
            print('hora incorreta.')
        else:
            while True:
                minuto = int(input('informe os minutos: '))
                if minuto < 0 or minuto > 59:
                    print('minuto incorreto.')
                else:
                    if hora > 12:
                        hora = hora - 12
                        horario = 'P'
                    else:
                        horario = 'A'
                    print(f'Horario convertido: {hora}:{minuto} {horario}.M')
                    break
            break


def main():
    sair = 'S'
    while sair == 'S':
        conversao()
        sair = input('deseja continuar? ').upper()

main()
