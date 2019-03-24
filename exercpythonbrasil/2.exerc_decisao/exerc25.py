'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''
def main():
    respostas = []
    perguntas = [
        "Telefonou para a vítima? ",
        "Esteve no local do crime? ",
        "Mora perto da vítima? ",
        "Devia para a vítima? ",
        "Já trabalhou com a vítima? "
    ]
    print("Responda S - SIM ou N - NÃO:")
    while True:
        for i in range(0, len(perguntas)):
            resp = input(f"{perguntas[i]}").upper()
            if resp == "S" or resp == 'N':
                respostas.append(resp)
            else:
                print('resposta não disponível!')
        break
    cont = respostas.count('S')
    if cont == 2:
        print('Suspeito!')
    elif cont == 3 or cont == 4:
        print('Cúmplice!')
    elif cont == 5:
        print('Assassino!')


main()
